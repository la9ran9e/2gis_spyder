### P2P Parser Client pseudocode

```python
class Peer:

    def check_turn(self):
        '''returns is this peer first in tracker queue'''
        pass
    
    def load_data(self, url):
        '''write data to stdout if url olready processed by other peers'''
        if self.check_url(url):
            # loading data
            pass
    
    
    def check_url(self, url):
        '''returns has url already processed by other peers'''
        pass


def main():
    client = Peer()
    while True:
        url = input()
        is_turn = client.check_turn()
        if not is_turn:
            client.load_data(url)
        else:
            print(url, flush=True)
```