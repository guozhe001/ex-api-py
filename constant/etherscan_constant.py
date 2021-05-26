# encoding=utf8

from constant import constant

ETHERSCAN_API = "https://api-cn.etherscan.com/api"

BSCSCAN_API = "https://api.bscscan.com/api"

# module
MODULE_CONTRACT = "contract"
MODULE_TRANSACTION = "transaction"
MODULE_PROXY = "proxy"

# action
ACTION_GET_SOURCECODE = "getsourcecode"
ACTION_GET_TX_RECEIPT_STATUS = "gettxreceiptstatus"
ACTION_GET_TRANSACTION_BY_HASH = "eth_getTransactionByHash"

# param
PARAM_MODULE = "?module="
PARAM_ACTION = "&action="
PARAM_ADDRESS = "&address="
PARAM_APIKEY = "&apikey="
PARAM_TXHASH = "&txhash="

# response key
RESPONSE_KEY_STATUS = "status"
RESPONSE_KEY_MESSAGE = "message"
RESPONSE_KEY_RESULT = "result"

# status code
SUCCESS_STATUS = "1"
FAIL_STATUS = "0"

# contact sourcecode result key
CONTRACT_SOURCECODE_KEY_SOURCECODE = "SourceCode"
CONTRACT_CONTENT = "content"

# contract sourcecode save path
CONTRACT_PATH = "contract"

# contract language file
CONTRACT_FILE_SUFFIX = ".sol"

exchange_api_mapping = {constant.EXCHANGE_BSCSCAN: BSCSCAN_API, constant.EXCHANGE_ETHERSCAN: ETHERSCAN_API}
