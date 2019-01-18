#!./venv/bin/python3
import socket
import random
import json

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

STORAGE = dict()


def get(address, message):
    url = message['data']
    peer_addresses = STORAGE.get(url, None)
    if not peer_addresses:
        SOCKET.sendto(b'0', address)
        return
    i = random.randint(0, len(peer_addresses)-1)
    peer_address = list(peer_addresses)[i]
    message = {'method': 'get', 'data': url, 'send_to': address}
    message = bytes(json.dumps(message), encoding='UTF-8')
    SOCKET.sendto(message, peer_address)


def post(address, message):
    data = message['data']
    to_address = tuple(message['send_to'])
    message = bytes(data, encoding='UTF-8')
    SOCKET.sendto(message, to_address)


def put(address, message):
    url = message['data']
    peer_addres = tuple(message['peer_address'])
    if url in STORAGE:
        STORAGE[url].add(peer_addres)
    else:
        STORAGE[url] = {peer_addres}


def peer(address, message):
    message = f'{address[0]}:{address[1]}'
    SOCKET.sendto(bytes(message, encoding='UTF-8'), address)


ROUTES = {
    'get': get,
    'post': post,
    'put': put,
    'peer': peer
}


def main():
    server_address = ('0.0.0.0', 10000)
    server_verbose = f'{server_address[0]}:{server_address[1]}'
    print(f'server started on {server_verbose}')
    SOCKET.bind(server_address)

    while True:
        print(f'{server_verbose} waiting for message...')
        message, address = SOCKET.recvfrom(1024)
        print(f'received {len(message)} bytes from {address}')
        print(f'message: {message}')
        message = json.loads(message.decode('UTF-8'))
        ROUTES[message['method']](address, message)


if __name__ == '__main__':
    main()