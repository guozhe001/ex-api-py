from unittest import TestCase

import etherscan_api


class Test(TestCase):
    def test_contract_code(self):
        response = etherscan_api.contract_code("0xB8c77482e45F1F44dE1745F52C74426C631bDD52")
        print(type(response))
        print(response)

    def test_get_url(self):
        expect = "https://api-cn.etherscan.com/api?module=contract&action=getsourcecode&address=0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413&apikey=YourApiKeyToken"
        url = etherscan_api.get_url("contract", "getsourcecode", "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413",
                                    "YourApiKeyToken")
        TestCase.assertEqual(self, expect, url, "")

    def test_get_and_save_contract_code(self):
        etherscan_api.get_and_save_contract_code("BNB", "0xB8c77482e45F1F44dE1745F52C74426C631bDD52")
