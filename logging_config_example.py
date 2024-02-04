import logging.config
import json

if __name__ == "__main__":
    with open(R"/path/to/json/config.json", "r") as file:
        config = json.load(file)

    logging.config.dictConfig(config)
    logger = logging.getLogger('monitoring') # make sure using right logger name
    logger.debug('This is a debug message')
