# -*- coding:utf-8 -*- 
# Author: Henry

from html.parser import HTMLParser
from urllib import request

class HTMLParserFromWeb(HTMLParser):
    def __init__(self):
        super().__init__()
        self.li = False
        self.h3 = False
        self.a = False
        self.p = False
        self.time = False
        self.span1 = False
        self.span2 = False
        self.event_dict = {}
        self.count = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'li':
            self.li = True
        elif tag == 'h3':
            for k, v in attrs:
                if k == 'class' and v == 'event-title':
                    self.h3 = True
        elif tag == 'a':
            self.a = True
        elif tag == 'p':
            self.p = True
        elif tag == 'time':
            self.time = True
        elif tag == 'span':
            for k, v in attrs:
                if k == 'class' and v == 'say-no-more':
                    self.span1 = True
                elif k == 'class' and v == 'event-location':
                    self.span2 = True

    def handle_endtag(self, tag):
        if tag == 'a':
            self.a = False
        elif tag == 'h3':
            self.h3 = False
        elif tag == 'span':
            self.span1 = False
            self.span2 = False
        elif tag == 'time':
            self.time = False
        elif tag == 'p':
            self.p = False
        elif tag == 'li':
            self.li = False

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_data(self, data):
        if self.li:
            if self.h3 == True and self.a == True:
                self.count += 1
                self.event_dict[self.count] = {}
                self.event_dict[self.count]['name'] = data
            elif self.p:
                if self.time:
                    if not self.span1:
                        self.event_dict[self.count]['time'] = data
                    else:
                        self.event_dict[self.count]['time'] += (',' + data)
                else:
                    if self.span2:
                        self.event_dict[self.count]['site'] = data

    def handle_comment(self, data):
        pass

    def handle_entityref(self, name):
        pass

    def handle_charref(self, name):
        pass

parser = HTMLParserFromWeb()

def parse_python_event(html_data):
    global parser
    parser = HTMLParserFromWeb()
    parser.feed(html_data)
    return parser.event_dict

if __name__ == '__main__':
    with request.urlopen('https://www.python.org/events/python-events/') as f:
        html_data_url = f.read()
    result = parse_python_event(html_data_url.decode('utf-8'))
    #print('Conference: %s' % result)
    for i in range(1, parser.count + 1):
        print(result[i]['name'], '\n', result[i]['time'], '\t', result[i]['site'])