# encoding=utf8
import json

from util import http_util

available = 1
disable = 0

REST_URL = "https://api.bithumb.com"

PAYMENT_CURRENCY_BTC = "BTC"
PAYMENT_CURRENCY_KRW = "KRW"

# bithumb提现的最小值，获取地址：https://apidocs.bithumb.com/docs/withdrawal_coin
MIN_WITHDRAWAL_QUANTITY = """BTC: 0.002 | ETH: 0.01 | LTC: 0.1 | ETC: 0.1 | XRP: 21 | BCH: 0.002 | BTG: 0.002 | EOS: 0.5 | ICX: 4 | TRX: 150 | ELF: 10 | OMG: 2 | GLM: 30 | ZIL: 30 | POWR: 23 | LRC: 42 | EOSDAC: 10 | STEEM: 0.01 | STRAX: 0.2 | ZRX: 6 | REP: 0.08 | XEM: 4 | SNT: 23 | ADA: 1 | BAT: 3 | WTC: 1.4 | LOOM: 22 | WAVES: 2 | TRUE: 10 | LINK: 0.11 | MEETONE: 10 | HORUS: 10 | ADD: 100 | RNT: 300 | ENJ: 2 | VET: 200 | MTL: 0.9 | CHL: 100 | BLACK: 10 | ATD: 100 | IOST: 1000 | TMTG: 360 | QKC: 2000 | HDAC: 200 | WET: 840 | AMO: 7000 | BSV: 0.002 | BXA: 15 | DAC: 670 | ORBS: 24 | TFUEL: 10 | VALOR: 5 | CON: 460 | ANKR: 27 | MIX: 360 | LAMB: 40 | CRO: 17 | FX: 10 | CHR: 12 | MBL: 3500 | MXC: 72 | WIN: 1 | DVP: 56 | FCT: 20 | FNB: 460 | TRV: 100 | PCM: 170 | DAD: 12 | AOA: 560 | XSR: 1300 | WOM: 15 | SOC: 360 | EM: 1000 | QBZ: 340 | BOA: 10 | FLETA: 180 | SXP: 0.9 | COS: 97 | APIX: 36 | EL: 170 | BASIC: 460 | HIVE: 18 | XPR: 800 | FIT: 720 | EGG: 360 | BORA: 17 | ARPA: 35 | APM: 100 | CKB: 170 | AERGO: 13 | ANW: 28 | CENNZ: 60 | EVZ: 44 | MCI: 170 | SRM: 0.7 | QTCON: 56 | UNI: 0.13 | YFI: 0.0001 | UMA: 0.17 | AAVE: 0.01 | COMP: 0.01 | REN: 5 | BAL: 0.08 | RSR: 59 | NMR: 0.07 | RLC: 2 | UOS: 9 | SAND: 7 | CVT: 18 | STPT: 63 | GOM2: 320 | RINGX: 28 | BEL: 0.8 | DVC: 11 | OBSR: 170 | ORC: 2 | POLA: 15 | AWO: 270 | ADP: 59 | DVI: 9 | IBP: 25 | GHX: 5 | MIR: 0.5 | CBK: 0.5 | ONX: 5 | MVC: 25 | BLY: 25 | WOZX: 3 | ANV: 2 | GRT: 3 | MM: 4 | BIOT: 77 | XNO: 12 | SNX: 0.2 | RAI: 2 | COLA: 5 | NU: 8 | OXT: 6 | LINA: 34 | MAP: 34 | AQT: 0.6 | WIKEN: 130 | MANA: 5 | LPT: 0.15 | MKR: 0.0014 | SUSHI: 0.23 | NSBT: 0.3 | DON: 2 | ASM: 9 | PUNDIX: 0.7 | CELR: 50 | ARW: 0.5 | MSB: 10 | RLY: 5 | OCEAN: 4 | BFC: 25 | ALICE: 0.4 | CHZ: 9 | BCD: 2 | GXC: 4 | BTT: 5000 | VSYS: 100 | IPX: 80 | WICC: 32 | ONT: 7 | LUNA: 12 | NEWS: 10 | AION: 35 | META: 300 | ONG: 25 | ALGO: 4 | JST: 250 | XTZ: 1.2 | MLK: 20 | WEMIX: 40 | DOT: 1.5 | SUN: 1 | ATOM: 1 | SSX: 42 | TEMCO: 2000 | LZM: 25 | HIBS: 250 | BURGER: 0.9"""

currency_min_withdrawal_quantity = dict()

for q in str.split(MIN_WITHDRAWAL_QUANTITY, "|"):
    c_list = q.strip().split(":")
    currency_min_withdrawal_quantity[c_list[0].strip()] = float(c_list[1].strip())


def get_ticker(order_currency, payment_currency):
    """
    获取指定交易对的ticker信息：https://apidocs.bithumb.com/docs/ticker
    https://api.bithumb.com/public/ticker/BTC_KRW
    :return:
    {
    "status":"0000",
    "data":{"opening_price":"63241000","closing_price":"63651000","min_price":"62944000","max_price":"65351000","units_traded":"2715.2835537","acc_trade_value":"173294332105.4152","prev_closing_price":"63239000","units_traded_24H":"3471.39085837","acc_trade_value_24H":"221565547379.3369","fluctate_24H":"418000","fluctate_rate_24H":"0.66","date":"1619687597790"}
    }
    """

    pass


def get_min_withdrawal(coin):
    """
    获取指定的资产的提现最小值
    :param coin: 提现的资产，如BTC、ETH
    :return:
        传入的单元最少可以提现多少
    """
    return currency_min_withdrawal_quantity[coin]


def get_asset_status(coin):
    url = "https://api.bithumb.com/public/assetsstatus/{}".format(coin)
    """
    获取资产的状态信息：https://apidocs.bithumb.com/docs/assets_status
    https://api.bithumb.com/public/assetsstatus/{order_currency}
    :param coin: 币
    :return:
    传入的币的状态
    {
    "status" : "0000",
    "data" :
    [
        {
            "deposit_status" : 1,
            "withdrawal_status" : 0
        }
    ]
    }
    """
    response = http_util.get(url)
    body = json.loads(response.text)
    # print(body)
    data = body["data"]
    return data["deposit_status"] == available, data["withdrawal_status"] == available
