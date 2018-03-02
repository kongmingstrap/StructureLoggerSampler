import json
import logging.config
import pathlib


class JsonLogger(object):
    def get_logger(self, name):
        config_file_path = str(pathlib.Path(__file__).parent.joinpath('logging.json').resolve())
        logging.config.dictConfig(json.load(open(config_file_path)))
        return logging.getLogger(name)
