import datetime

import moment
import pytz

date_format = '%Y-%m-%d %H:%M:%S'

DATE_FORMAT_T = "YYYY-MM-DDTHH:%M:%S.%f"

TIME_ZONE = "Asia/Shanghai"


def format_unix_datetime(format_pattern, unix_timestamp):
    """
    格式化unix时间戳

    Args:
      format_pattern (str): 目标日期格式
      unix_timestamp (int): Unix 时间戳，毫秒

    Returns:
      格式化后的字符串
    """
    return format_unix_datetime_from_second(format_pattern, int(unix_timestamp / 1000))


def format_unix_datetime_from_second(format_pattern, utc_timestamp):
    """
    格式化unix时间戳

    Args:
      format_pattern (str): 目标日期格式
      utc_timestamp (int): Unix 时间戳, 单位秒

    Returns:
      格式化后的字符串
    """
    temp_dt = datetime.datetime.utcfromtimestamp(utc_timestamp)
    utc_tz = pytz.timezone('UTC')

    # 将时区变更为 utc 时区
    utc_dt = temp_dt.replace(tzinfo=utc_tz)

    # 转化为上海时区时间
    shanghai_dt = utc_dt.astimezone(pytz.timezone(TIME_ZONE))  # 直接转带时区的时间

    return shanghai_dt.strftime(format_pattern)


# unix_timestamp参数的单位是毫秒：1603227600000
def format_default_datetime(unix_timestamp):
    return format_unix_datetime(date_format, unix_timestamp)


# second参数的单位是秒：1603227600
def timestamp_to_str(second):
    return format_unix_datetime_from_second(date_format, second)


# 获取当前时间：格式为2020-12-08T09:08:57.715Z
def get_now():
    timestamp = now().format(DATE_FORMAT_T)[:-3] + "Z"
    return timestamp


# 获取当前时间，格式为2014-11-06T10:34:47.123456Z
def get_now_iso_8601(date_time):
    return date_time.format(DATE_FORMAT_T) + "Z"


def now():
    return moment.utcnow()


def get_now_timestamp():
    return moment_to_timestamp(now())


def moment_to_timestamp(m):
    return round(m.datetime.timestamp() * 1000)


def to_timestamp(date_str):
    return moment_to_timestamp(str_to_date(date_str))


def str_to_date(s):
    return moment.date(s)


def str_to_utc_date(s):
    return moment.utc(s)


def timestamp_to_date(timestamp):
    return moment.date(timestamp)


def to_utc_date(timestamp):
    return moment.unix(timestamp, utc=True)
