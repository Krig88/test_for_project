# AICDW 
## Adventures In Cat-Dog-World
    description

## Run the script
    1) install tensorflow: `pip install tensorflow`
    2) run main file `python3 main.py`

## Available options
    usage: main.py [-h] [-l LOG_DIR] [-c CONFIG_FILE]
    
    Adventures In Cat Dog World
    
    options:
      -h, --help            show this help message and exit
      -l LOG_DIR, --log_dir LOG_DIR
                            provide a name (path) for logs directory
      -c CONFIG_FILE, --config_file CONFIG_FILE
                            provide a name (path) for config file


## Configurations
```JSON
{
  "Environment": {
    "Connectedness": 4,
    "topology_function": ""
  },
  "Field": {
    "size": [4,4],
    "walls": {
      "coordinates": [
        [0,0],
        [1,1]
      ]
    }
  },
  "controllers": [
    
    {"ControllerName1": [ 
      {"ActorType1":  [0, 0]},
      {"ActorType1":  [0, 0]}
    ]},
    {"ControllerName2": [
      {"ActorType2":  [0, 0]}
    ]}
  ]
}
```
- Connectedness can be 4 or 8
- topology_function is not implemented yet
- ControllerName is one of "AgentController", "CatDog", "RandomController" or "KeyboardController"
- ActorType is one of "Cat", "Dog" or "Player"