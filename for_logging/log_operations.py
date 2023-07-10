import logging
import os
import shutil
import for_logging.agents_statistic as a_stat

from dataclasses import dataclass


@dataclass
class LogConfig:
    log_dir: str = None
    cur_handler = None
    statistic_logger = None


def log_init(log_dir: str = "logs"):
    LogConfig.log_dir = log_dir

    if os.path.isdir(log_dir):
        clear_folder(log_dir)
    else:
        os.makedirs(log_dir)

    logging.basicConfig(level=logging.INFO, filename=log_dir + '/game0.log', filemode='w')
    LogConfig.statistic_logger = setup_custom_logger('stat_log', 15, log_dir + '/game_statistic.log')


def clear_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except:
            # TODO: правильно обработать исключения
            pass


def change_logging_file(file_name):
    if LogConfig.cur_handler is not None:
        LogConfig.cur_handler.close()
        logging.getLogger().removeHandler(LogConfig.cur_handler)
    new_handler = logging.FileHandler(LogConfig.log_dir + "/" + file_name)
    logging.getLogger().addHandler(new_handler)
    LogConfig.cur_handler = new_handler


def setup_custom_logger(name, level, log_file):
    logging.addLevelName(level, name.upper())

    def custom(self, message, *args, **kws):
        if self.isEnabledFor(level):
            self._log(level, message, args, **kws)

    setattr(logging.Logger, name, custom)
    logger = logging.getLogger(__name__)
    logger.setLevel(level)
    handler = logging.FileHandler(log_file)
    handler.setLevel(level)
    logger.addHandler(handler)
    return logger


def log_game_statistic(game_number: int):
    if LogConfig.statistic_logger is None:
        LogConfig.statistic_logger = setup_custom_logger('stat_log', 15, LogConfig.log_dir + '/game_statistic.log')
    # LogConfig.statistic_logger.stat_log()
    LogConfig.statistic_logger.stat_log(f"Game number{game_number}")
    a_stat.update_score()
    for counter, i in enumerate(a_stat.agents_statistic_folder):
        stat = a_stat.agents_statistic_folder[i]
        LogConfig.statistic_logger.stat_log(f"cats: {stat.cats}")
        LogConfig.statistic_logger.stat_log(f"dogs: {stat.dogs}")
        LogConfig.statistic_logger.stat_log(f"skips: {stat.skips}")
        LogConfig.statistic_logger.stat_log(f"agent{counter} score:{stat.score}")
        LogConfig.statistic_logger.stat_log(f"steps:{stat.steps}")
        LogConfig.statistic_logger.stat_log("------------------------------")
    a_stat.agents_statistic_folder.clear()
