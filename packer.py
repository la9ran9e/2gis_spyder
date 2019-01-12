#!./venv/bin/python3
import sys
import hashlib


def main():
    for line in sys.stdin:
        url, data = line.rstrip().split('|')
        url_hash = hashlib.md5(bytes(url, encoding='UTF-8')).hexdigest()
        with open(f'storage/{url_hash}', 'w') as file:
            file.write(data)


if __name__ == '__main__':
    main()
