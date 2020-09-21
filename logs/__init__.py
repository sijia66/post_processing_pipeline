import json
import logging
import logging.config




def get_a_logger():
    '''
    log_file_path(string) : default to the same folder
    '''
    json_obj = json.loads(config_string)
    #set the log into the dictionary

    logging.config.dictConfig(json_obj)

    return logging.getLogger(__name__)


config_string = '''
{
    "version": 1,
    "disable_existing_loggers": false,
    "formatters": {
        "simple": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },
 
    "handlers": {
        "file_handler": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "filename": "python_logging.log",
            "encoding": "utf8"
        }
    },
 
    "root": {
        "level": "DEBUG",
        "handlers": ["file_handler"]
    }
}

'''
if __name__ == "__main__":
    logger = get_a_logger()
    logger.info('Can set up the logger!')
