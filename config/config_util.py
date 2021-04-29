# encoding=utf8

import configparser
import os

from constant import constant

module_path = os.path.abspath(os.path.join('.'))
config = configparser.ConfigParser()

config.read(module_path + "/config/api_key_config.ini")


def get(section, key):
    return config[section][key]


def list_sections():
    return config.sections()


# 获取指定交易所的apikey和secret
def get_api_key_secret(exchange):
    section = get_section([constant.CONFIG_API, exchange])
    return get(section, constant.CONFIG_API_KEY), get(section, constant.CONFIG_SECRET)


# 根据key获取section
def get_section(key_list):
    return str.join(constant.CONFIG_SPLIT, key_list)
