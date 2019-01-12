#!./venv/bin/python3
import sys
import json
import requests
from parser.base import Parser


def main():
    # TODO: SIGINT handler
    config_path = get_args()
    config = get_filter(config_path)
    content_cls_name = config['content_cls_name']
    name_filter = config.get('map', None) or config.get('names', None)
    for line in sys.stdin:
        url = line.rstrip()
        headers = config.get('headers', None)
        encoding = config.get('encoding', 'utf-8')
        raw_content = get_content(url, headers, encoding)
        content = parser(raw_content, content_cls_name)
        if isinstance(name_filter, list):
            content = list_filter(content, name_filter)
        elif isinstance(name_filter, dict):
            content = mapper(content, name_filter)
        filtered_str = json.dumps(content, ensure_ascii=False)
        print(f'{url}|{filtered_str}', flush=True)


def get_args():
    if len(sys.argv) > 1:
        return sys.argv[1]


def get_filter(config):
    with open(config, 'rb') as f:
        return json.load(f)


def get_content(url, headers=None, encoding='utf-8'):
    res = requests.get(url, headers=headers)
    res.encoding = encoding
    return res.text


def parser(content, content_cls_name):
    p = Parser(content_cls_name)
    try:
        p.feed(content)
    except StopIteration:
        pass
    return p.result


def list_filter(content, name_filter):
    res = {key: value for key, value in content.items() if key in name_filter}
    return res


def mapper(content, name_mapper):
    res = {name_mapper[key]: value for key, value in content.items() if key in name_mapper}
    return res


if __name__ == '__main__':
    main()
