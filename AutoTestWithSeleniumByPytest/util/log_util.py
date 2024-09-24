# -*-coding:utf-8-*-
from datetime import datetime
from config.build_config import BuildConfig
import logging
import logging.config
import yaml


class LogUtil:
    @staticmethod
    def get_logger(name):
        """
        修改输出到的文件的文件名以日期命名,文件存放至相对文件log文件夹下
        :param name: logger名
        :return:
        """
        # error的文件设置比较合理
        config_path =BuildConfig.LOGGING_CONFIG
        with open(config_path, 'rt') as f:
            config = yaml.safe_load(f.read())
            log_path = BuildConfig.LOGGING_PATH
            now = datetime.now()
            log_error_file_name = f"{log_path}error.{now.strftime('%Y-%m-%d')}.log"
            log_info_file_name = f"{log_path}info.{now.strftime('%Y-%m-%d')}.log"
            config["handlers"]["h_error"]["filename"] = log_error_file_name
            config["handlers"]["h_info"]["filename"] = log_info_file_name
        logging.config.dictConfig(config)
        return logging.getLogger(name)

    @staticmethod
    def is_debug_enabled():
        """
        是否需要日志
        :return: True=需要日志
                 False=不需要日志
        """
        return BuildConfig.DEBUG


    @staticmethod
    def info(msg):
        """
        记录到info日志里
        :param msg:需要记录的信息
        :return:
        """
        if not LogUtil.is_debug_enabled():
            return
        logger = LogUtil.get_logger("logger_info")
        logger.info(msg)

    @staticmethod
    def error(msg):
        """引入Error日志"""
        if not LogUtil.is_debug_enabled():
            return
        logger = LogUtil.get_logger("logger_error")
        logger.error(msg, exc_info=True)


if __name__ == "__main__":
    LogUtil.error("出错了")
    LogUtil.info("info测试")




