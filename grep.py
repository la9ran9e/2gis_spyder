#!./venv/bin/python3
import sys
import json
import requests
from parser.base import Parser


def main():
    filter_conf_path = get_args()
    filter_conf = get_filter(filter_conf_path)
    while True:
        url = input()
        headers = filter_conf.get('headers', None)
        encoding = filter_conf.get('encoding', 'utf-8')
        content = get_content(url, headers, encoding)
        filtered = content_filter(content, filter_conf)
        filtered_str = json.dumps(filtered, ensure_ascii=False)
        print(filtered_str, flush=True)


def get_args():
    if len(sys.argv) > 1:
        return sys.argv[1]


def get_filter(filter_conf):
    with open(filter_conf, 'rb') as f:
        return json.load(f)


def get_content(url, headers=None, encoding='utf-8'):
    res = requests.get(url, headers=headers)
    res.encoding = encoding
    return res.text


def content_filter(content, filter_conf):
    parser = Parser(filter_conf['content_cls_name'])
    try:
        parser.feed(content)
    except StopIteration:
        pass
    name_filter = filter_conf.get('names', None)
    if not name_filter:
        res = parser.result
    else:
        res = {key: value for key, value in parser.result.items() if key in name_filter}
    return res


if __name__ == '__main__':
    main()
