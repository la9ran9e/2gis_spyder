#!./venv/bin/python3
import socket
import json
import sys
import hashlib
from packer import packer
from datetime import datetime


SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
SERVER_ADDRESS = ('localhost', 10000)


def get_peer():
    with open('peer_address', 'r') as f:
        address = f.read().split(':')
    return tuple([address[0], int(address[1])])


PEER_ADDRESS = get_peer()


def arg_parser():
    return sys.argv[1]


def get(url):
    url_hash = hashlib.md5(bytes(url, encoding='UTF-8')).hexdigest()
    message = {'method': 'get', 'data': url_hash}
    message = json.dumps(message)
    message = bytes(message, encoding='UTF-8')
    print('sending {!r}'.format(message), file=sys.stderr)
    SOCKET.sendto(message, SERVER_ADDRESS)
    data, server = SOCKET.recvfrom(4096)
    now = datetime.now()
    print(f'received: {data} at {now}', file=sys.stderr)
    if data == b'0':
        print(url, flush=True)
    else:
        packer(url_hash, data.decode('UTF-8'))
        put(url_hash)


def put(url_hash):
    message = {'method': 'put', 'data': url_hash, 'peer_address': PEER_ADDRESS}
    message = json.dumps(message)
    message = bytes(message, encoding='UTF-8')
    print('sending {!r}'.format(message), file=sys.stderr)
    SOCKET.sendto(message, SERVER_ADDRESS)


ROUTE = {
    'get': get,
    'put': put
}


def main():
    print(f'started: {datetime.now()}', file=sys.stderr)
    arg = arg_parser()
    method = ROUTE[arg]

    def loop():
        while True:
            url = input()
            method(url)
    try:
        loop()
    except EOFError:
        print(f'finished: {datetime.now()}', file=sys.stderr)


if __name__ == '__main__':
    main()
