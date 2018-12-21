#!./venv/bin/python3.6
import sys
import requests
from lxml import etree


# SITEMAP_URL = 'https://2gis.ru/sitemap.xml'
# CITY = "moscow"
# NAME = "districts"


def main():
    args = get_args()
    urls = find(*args)
    if urls:
        download(urls)


def get_args():
    if len(sys.argv) == 2:
        return parse_config(sys.argv[1])
    if len(sys.argv) < 4:
        print('Expected: sitemap url, city, object type name')
        exit(0)
    return sys.argv[1:]


def parse_config(config_file):
    raise Exception(NotImplemented)


def find(city, name, url):

    def _find(name, url):
        result = []
        res = requests.get(url)
        xml = etree.fromstring(res.content)
        rec_find(name, xml, result)
        return result

    def rec_find(name, obj, result):
        for i in obj.getchildren():
            if i.text is None:
                rec_find(name, i, result)
            else:
                if name in i.text:
                    result.append(i.text)

    result = _find(city, url)
    if result:
        return _find(name, result[0])


def download(urls):

    def rec_find(obj):
        for i in obj.getchildren():
            if i.text is None:
                rec_find(i)
            else:
                if 'loc' in i.tag:
                    print(i.text, flush=True)

    for url in urls:
        res = requests.get(url)
        xml = etree.fromstring(res.content)
        rec_find(xml)


if __name__ == '__main__':
    main()
