from unittest import TestCase
from util import date_util


class Test(TestCase):
    def test_timestamp_to_date(self):
        print(date_util.format_default_datetime(1623945600000))
