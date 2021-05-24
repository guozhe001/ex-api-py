from unittest import TestCase

import etherscan_api
from constant import constant


class Test(TestCase):
    def test_contract_code(self):
        response = etherscan_api.contract_code(constant.EXCHANGE_ETHERSCAN,
                                               "0xB8c77482e45F1F44dE1745F52C74426C631bDD52")
        print(type(response))
        print(response)

    def test_get_url(self):
        expect = "https://api-cn.etherscan.com/api?module=contract&action=getsourcecode&address=0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413&apikey=YourApiKeyToken"
        url = etherscan_api.get_url(constant.EXCHANGE_ETHERSCAN, "contract", "getsourcecode",
                                    "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413",
                                    "YourApiKeyToken")
        TestCase.assertEqual(self, expect, url, "")
        print(url)

    def test_get_and_save_contract_code(self):
        etherscan_api.get_and_save_contract_code(constant.EXCHANGE_ETHERSCAN, "BNB",
                                                 "0xB8c77482e45F1F44dE1745F52C74426C631bDD52")

    def test_get_transaction(self):
        etherscan_api.get_transaction(constant.EXCHANGE_ETHERSCAN, "0xce5182106a73e94dae40d19c0028ccf74cb1cc0e")
