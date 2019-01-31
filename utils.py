import os
import time
import socket


def open_callback(name, ns=('get', 'put'), domain='./callback.sock',
                  sock_timeout=0.25, connect_delay=0.15):
    def _rm(self):
        self.close()
        try:
            os.remove(self.domain)
        except FileNotFoundError:
            pass

    def _wrap(self, func, method_name, arg):
        method = getattr(self, method_name)

        def wrapper(*args, **kwargs):
            if not func(*args, **kwargs):
                method(arg)
        return wrapper

    callback = type('callback', (socket.socket,), {'domain': domain, 'rm': _rm, 'wrap': _wrap})
    cb = callback(socket.AF_UNIX, socket.SOCK_DGRAM)
    cb.settimeout(sock_timeout)
    if name == ns[0]:
        cb.bind(domain)
        try:
            cb.recv(1)
        except socket.timeout:
            cb.rm()
            return
    elif name == ns[1]:
        time.sleep(connect_delay)
        try:
            cb.connect(domain)
        except FileNotFoundError:
            return
        cb.send(b'1')
    else:
        raise KeyError(f'name {name} not found in namespace {ns}')
    cb.settimeout(None)
    return cb


def read_peer(path='./peer_address'):
    with open(path, 'r') as f:
        address = f.read().split(':')
    return tuple([address[0], int(address[1])])
