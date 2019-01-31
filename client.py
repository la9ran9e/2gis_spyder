#!./venv/bin/python3
import sys
import json
import socket
import hashlib
from utils import open_callback, read_peer
from packer import packer


def main():
    arg = sys.argv[1]
    callback = open_callback(arg)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 10000)
    peer_address = read_peer()
    if arg == 'get':
        method = callback.wrap(get, 'recv', 1) if callback else get
    elif arg == 'put':
        method = callback.wrap(get, 'send', b'1') if callback else put
    else:
        raise KeyError(f'wrong method: {arg}')
    try:
        run(method, sock, server_address, peer_address)
    finally:
        sock.close()
        if callback:
            callback.rm()


def get(url, sock, server_address, peer_address):
    url_hash = hashlib.md5(bytes(url, encoding='UTF-8')).hexdigest()
    message = {'method': 'get', 'data': url_hash}
    message = json.dumps(message)
    message = bytes(message, encoding='UTF-8')
    print('sending {!r}'.format(message), file=sys.stderr)
    sock.sendto(message, server_address)
    data, server = sock.recvfrom(4096)
    if data == b'0':
        print(url, flush=True)
        return 0
    else:
        packer(url_hash, data.decode('UTF-8'))
        put(url_hash, sock, server_address, peer_address)
        return 1


def put(url_hash, sock, server_address, peer_address):
    message = {'method': 'put', 'data': url_hash, 'peer_address': peer_address}
    message = json.dumps(message)
    message = bytes(message, encoding='UTF-8')
    print('sending {!r}'.format(message), file=sys.stderr)
    sock.sendto(message, server_address)
    return 0


def run(method, *args, **kwargs):
    for line in sys.stdin:
        url = line.rstrip()
        method(url, *args, **kwargs)


if __name__ == '__main__':
    main()
