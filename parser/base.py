from html.parser import HTMLParser as BaseParser


class Parser(BaseParser):
    _div = 0
    _cls_name = None
    result = {}

    def __init__(self, content_cls_name, *args, **kwargs):
        self.content_cls_name = content_cls_name
        super().__init__(*args, **kwargs)

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            for attr in attrs:
                if attr[0] == 'class':
                    if attr[1] == self.content_cls_name:
                        self._div += 1
                        self._cls_name = attr[1]
                    else:
                        if self._div > 0:
                            self._div += 1
                            self._cls_name = attr[1]
                    return

    def handle_data(self, data):
        if self._div > 0:
            self.result[self._cls_name] = data

    def handle_endtag(self, tag):
        if tag == 'div' and self._div > 0:
            if self._div > 1:
                self._div -= 1
            elif self._div == 1:
                raise StopIteration