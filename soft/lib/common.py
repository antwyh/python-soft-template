import json
import logging
import logging.config
from conf import settings


def get_logger(name):
    logging.config.dictConfig(settings.LOGGING_DIC)
    logger = logging.getLogger(name)  # 生成 log 实例
    return logger


def conn_db():
    db_path = settings.DB_PATH
    dic = json.load((open(db_path, 'r', encoding='utf-8')))
    return dic
