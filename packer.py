#!./venv/bin/python3
import hashlib


def main():
    def loop():
        while True:
            url, data = input().split('|')
            url_hash = hashlib.md5(bytes(url, encoding='UTF-8')).hexdigest()
            packer(url_hash, data)
            print(url_hash, flush=True)
    try:
        loop()
    except EOFError:
        pass


def packer(url_hash, data):
    with open(f'storage/{url_hash}', 'w') as file:
        file.write(data)


if __name__ == '__main__':
    main()
