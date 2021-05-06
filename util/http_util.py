# encoding=utf8

# get请求
import requests


def get_with_headers(url, headers, payload):
    return requests.request("GET", url, headers=headers, data=payload)


def get(url):
    print("url={}".format(url))
    return get_with_headers(url, None, None)
