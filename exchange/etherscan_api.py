# encoding=utf8
import json
import os

from config import config_util
from constant import etherscan_constant, constant
from util import http_util, file_util


def get_c_url(ex, module, action, address):
    if module is None:
        raise BaseException("etherscan的module参数不能为空")
    url = etherscan_constant.exchange_api_mapping.get(ex) + "?module=" + module

    if action is not None:
        url = url + etherscan_constant.PARAM_ACTION + action

    if address is not None:
        url = url + etherscan_constant.PARAM_ADDRESS + address

    apikey = get_apikey(ex)
    if apikey is not None:
        url = url + etherscan_constant.PARAM_APIKEY + apikey

    return url


def get_contract_url(ex, action, address):
    return get_c_url(ex, etherscan_constant.MODULE_CONTRACT, action, address)


def contract_code(ex, address):
    """
    根据合约地址获取合约源代码
    :param ex 交易所，此处表示在哪个链
    :param address: 合约地址
    :return: 合约代码
    """
    url = get_contract_url(ex, etherscan_constant.ACTION_GET_SOURCECODE, address, )
    response = http_util.get(url)
    body = json.loads(response.text)
    if body[etherscan_constant.RESPONSE_KEY_STATUS] is etherscan_constant.SUCCESS_STATUS:
        result = body[etherscan_constant.RESPONSE_KEY_RESULT]
        if isinstance(result, list):
            sourcecode = result[0][etherscan_constant.CONTRACT_SOURCECODE_KEY_SOURCECODE]
            try:
                return json.loads(sourcecode)
            except json.decoder.JSONDecodeError:
                return sourcecode
    return None


def check_if_exits(ex, name):
    return file_util.exists(get_contract_code_file_path(ex, name, (get_file_name(name))))


def get_contract_code_file_path(ex, name, filename):
    return os.path.join("..", etherscan_constant.CONTRACT_PATH, ex, name, filename)


def get_file_name(name):
    return name + etherscan_constant.CONTRACT_FILE_SUFFIX


def get_and_save_contract_code(ex, name, address):
    """
    根据合约地址获取并保存合约源代码
    :param ex 交易所，此处表示在哪个链
    :param name 合约名称
    :param address: 合约地址
    :return:
    """
    if check_if_exits(ex, name):
        print("name={}, address={} is exits".format(name, address))
    else:
        code = contract_code(ex, address)
        if code is not None:
            if isinstance(code, dict):
                for filename in code:
                    file_util.write(get_contract_code_file_path(ex, name, filename),
                                    code[filename][etherscan_constant.CONTRACT_CONTENT])
            else:
                file_util.write(get_contract_code_file_path(ex, name, get_file_name(name)), code)


def get_apikey(ex):
    return config_util.get_api_key(ex)


def get_all_wanted_contract_code(ex):
    wanted_section = config_util.list_all(config_util.get_section([constant.CONFIG_WANTED, ex]))
    for k in wanted_section:
        get_and_save_contract_code(ex, k, wanted_section[k])


def get_tx_url(ex, module, action, txhash):
    if module is None:
        raise BaseException("etherscan的module参数不能为空")
    url = etherscan_constant.exchange_api_mapping.get(ex) + "?module=" + module

    if action is not None:
        url = url + etherscan_constant.PARAM_ACTION + action

    if txhash is not None:
        url = url + etherscan_constant.PARAM_TXHASH + txhash

    apikey = get_apikey(ex)
    if apikey is not None:
        url = url + etherscan_constant.PARAM_APIKEY + apikey

    return url


def get_url(ex, module, action, params):
    if module is None:
        raise BaseException("etherscan的module参数不能为空")
    url = etherscan_constant.exchange_api_mapping.get(ex) + "?module=" + module

    if action is not None:
        url = url + etherscan_constant.PARAM_ACTION + action

    for param in params:
        url = url + param + params[param]

    apikey = get_apikey(ex)
    if apikey is not None:
        url = url + etherscan_constant.PARAM_APIKEY + apikey

    return url


def check_transaction_receipt_status(ex, txhash):
    url = get_tx_url(ex, etherscan_constant.MODULE_TRANSACTION, etherscan_constant.ACTION_GET_TX_RECEIPT_STATUS, txhash)
    response = http_util.get(url)
    return json.loads(response.text)


def get_transaction(ex, txhash):
    url = get_url(ex, etherscan_constant.MODULE_PROXY, etherscan_constant.ACTION_GET_TRANSACTION_BY_HASH,
                  {etherscan_constant.PARAM_TXHASH: txhash})
    response = http_util.get(url)
    return json.loads(response.text)


if __name__ == '__main__':
    get_all_wanted_contract_code(constant.EXCHANGE_BSCSCAN)
    # code = contract_code(constant.EXCHANGE_BSCSCAN, "0x819eea71d3f93bb604816f1797d4828c90219b5d")
    # print(type(code))
    # print(code)
