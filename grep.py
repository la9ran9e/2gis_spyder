#!./venv/bin/python3.6
import sys
import json
import requests
from parser.base import Parser


def main():
    filter_conf_path = get_args()
    filter_conf = get_filter(filter_conf_path)
    while True:
        url = input()
        content = get_content(url)
        filtered = content_filter(content, filter_conf)
        filtered_str = json.dumps(filtered)
        print(filtered_str, flush=True)


def get_args():
    if len(sys.argv) > 1:
        return sys.argv[1]


def get_filter(filter_conf):
    return json.load(open(filter_conf, 'rb'))


def get_content(url):
    res = requests.get(url)
    return res.text


def content_filter(content, filter_conf):
    parser = Parser(filter_conf['content_cls_name'])
    try:
        parser.feed(content)
    except StopIteration:
        pass
    if not filter_conf:
        res = parser.result
    else:
        filter_list = filter_conf['names']
        res = {key: value for key, value in parser.result.items() if key in filter_list}
    return res


if __name__ == '__main__':
    main()
