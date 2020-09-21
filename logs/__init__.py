import json
import logging
import logging.config

#TO-DO
#nd to write a test 


def set_up_loging():
    '''
    log_file_path(string) : default to the same folder
    '''
    json_obj = json.loads(config_string)
    #set the log into the dictionary

    logging.config.dictConfig(json_obj)


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
    set_up_loging()
    logger = logging.getLogger(__name__)
    logger.info('what do you think')