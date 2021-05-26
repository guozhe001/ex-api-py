from unittest import TestCase

import etherscan_api
from constant import constant, etherscan_constant


class Test(TestCase):
    def test_contract_code(self):
        response = etherscan_api.contract_code(constant.EXCHANGE_ETHERSCAN,
                                               "0xB8c77482e45F1F44dE1745F52C74426C631bDD52")
        print(type(response))
        print(response)

    def test_get_c_url(self):
        expect = "https://api-cn.etherscan.com/api?module=contract&action=getsourcecode&address=0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413&apikey=NT1V11IJ3IJM1RFC3B54RCPU8JE54JKXT5"
        url = etherscan_api.get_c_url(constant.EXCHANGE_ETHERSCAN, "contract", "getsourcecode",
                                      "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413")
        TestCase.assertEqual(self, expect, url, "")
        print(url)

    def test_get_url(self):
        expect = "https://api.bscscan.com/api?module=proxy&action=eth_getTransactionByHash&txhash=0xa0f2e87dfb75e3ebb8b23eff7b490442ff74cf8921eb61217dfc48918fe4020f&apikey=V7377MF819S1EXYCKW3TQJ5WRQA58GWR9X"
        url = etherscan_api.get_url(constant.EXCHANGE_BSCSCAN, etherscan_constant.MODULE_PROXY,
                                    etherscan_constant.ACTION_GET_TRANSACTION_BY_HASH,
                                    {
                                        etherscan_constant.PARAM_TXHASH:
                                            "0xa0f2e87dfb75e3ebb8b23eff7b490442ff74cf8921eb61217dfc48918fe4020f"})
        TestCase.assertEqual(self, expect, url, "")

    def test_get_and_save_contract_code(self):
        etherscan_api.get_and_save_contract_code(constant.EXCHANGE_ETHERSCAN, "BNB",
                                                 "0xB8c77482e45F1F44dE1745F52C74426C631bDD52")

    def test_check_transaction_receipt_status(self):
        response = etherscan_api.check_transaction_receipt_status(constant.EXCHANGE_BSCSCAN,
                                                                  "0xce5182106a73e94dae40d19c0028ccf74cb1cc0e")
        print(response)
        TestCase.assertEqual(self, etherscan_constant.SUCCESS_STATUS,
                             response[etherscan_constant.RESPONSE_KEY_STATUS], "")

    def test_get_transaction(self):
        transaction = etherscan_api.get_transaction(constant.EXCHANGE_BSCSCAN,
                                                    "0xfbe65ad3eed6b28d59bf6043debf1166d3420d214020ef54f12d2e0583a66f13")
        print(transaction)
        result = transaction[etherscan_constant.RESPONSE_KEY_RESULT]
        print(result)
        print(type(result))
        for k in result:
            print(k, result[k])
