import logging
import os
import shutil
from dataclasses import dataclass


@dataclass
class LogConfig:
    log_dir: str = None


def log_init(log_dir: str = "logs"):
    LogConfig.log_dir = log_dir

    if os.path.isdir(log_dir):
        clear_folder(log_dir)
    else:
        os.makedirs(log_dir)

    logging.basicConfig(level=logging.INFO, filename=log_dir + '/game0.log', filemode='w')


def clear_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception:
            pass


