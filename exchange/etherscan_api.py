# encoding=utf8
import json
import os

from config import config_util
from constant import etherscan_constant, constant
from util import http_util, file_util


def get_url(module, action, address, apikey):
    if module is None:
        raise BaseException("etherscan的module参数不能为空")
    url = etherscan_constant.ETHERSCAN_API + "?module=" + module

    if action is not None:
        url = url + etherscan_constant.PARAM_ACTION + action

    if address is not None:
        url = url + etherscan_constant.PARAM_ADDRESS + address

    if apikey is not None:
        url = url + etherscan_constant.PARAM_APIKEY + apikey

    return url


def get_contract_url(action, address, apikey):
    return get_url(etherscan_constant.MODULE_CONTRACT, action, address, apikey)


def contract_code(address):
    """
    根据合约地址获取合约源代码
    :param address: 合约地址
    :return: 合约代码
    """
    url = get_contract_url(etherscan_constant.ACTION_GET_SOURCECODE, address, get_apikey())
    response = http_util.get(url)
    body = json.loads(response.text)
    if body[etherscan_constant.RESPONSE_KEY_STATUS] is etherscan_constant.SUCCESS_STATUS:
        result = body[etherscan_constant.RESPONSE_KEY_RESULT]
        if isinstance(result, list):
            return result[0][etherscan_constant.CONTRACT_SOURCECODE_KEY_SOURCECODE]
    return None


def check_if_exits(name):
    return file_util.exists(get_contract_code_file_name(name))


def get_contract_code_file_name(name):
    return os.path.join("..", etherscan_constant.CONTRACT_PATH, name,
                        name + etherscan_constant.CONTRACT_FILE_SUFFIX)


def get_and_save_contract_code(name, address):
    """
    根据合约地址获取并保存合约源代码
    :param name 合约名称
    :param address: 合约地址
    :return:
    """
    if check_if_exits(name):
        print("name={}, address={} is exits".format(name, address))
    else:
        code = contract_code(address)
        file_util.write(get_contract_code_file_name(name), code)


def get_apikey():
    return config_util.get_api_key(constant.EXCHANGE_ETHERSCAN)


def get_all_wanted_contract_code():
    section = config_util.list_all(constant.CONFIG_WANTED)
    for k in section:
        get_and_save_contract_code(k, section[k])


if __name__ == '__main__':
    get_all_wanted_contract_code()
