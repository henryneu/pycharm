# -*- coding:utf-8 -*- 
# Author: Henry

from xml.parsers.expat import ParserCreate
from urllib import request

class WeatherSaxHandler(object):
    def __init__(self):
        self.weather = {}
        self.daycount = 1

    def start_element(self, name, attrs):
        if 'location' in name:
            self.weather['city'] = attrs['city']
            self.weather['country'] = attrs['country']
        if 'forecast' in name and self.daycount:
            daykey = 'today' if self.daycount == 1 else 'tomorrow'
            self.weather[daykey] = {'text': attrs['text'], 'low': int(attrs['low']), 'high': int(attrs['high'])}
            self.daycount = 2 if self.daycount == 1 else 0

def fetch_xml(url):
    with request.urlopen(url) as f:
        data = f.read()
        return data.decode('utf-8')

def parse_weather(xml):
    # return {
    #     'city': 'Beijing',
    #     'country': 'China',
    #     'today': {
    #         'text': 'Partly Cloudy',
    #         'low': 20,
    #         'high': 33
    #     },
    #     'tomorrow': {
    #         'text': 'Sunny',
    #         'low': 21,
    #         'high': 34
    #     }
    # }

    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.Parse(xml)
    return handler.weather

# 硬编码data数据
data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
    <channel>
        <title>Yahoo! Weather - Beijing, CN</title>
        <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
        <yweather:location city="Beijing" region="" country="China"/>
        <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
        <yweather:wind chill="28" direction="180" speed="14.48" />
        <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
        <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
        <item>
            <geo:lat>39.91</geo:lat>
            <geo:long>116.39</geo:long>
            <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
            <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
            <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
            <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
            <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
            <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
            <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
        </item>
    </channel>
</rss>
'''
#weather = parse_weather(data)
# assert weather['city'] == 'Beijing', weather['city']
# assert weather['country'] == 'China', weather['country']
# assert weather['today']['text'] == 'Partly Cloudy', weather['today']['text']
# assert weather['today']['low'] == 20, weather['today']['low']
# assert weather['today']['high'] == 33, weather['today']['high']
# assert weather['tomorrow']['text'] == 'Sunny', weather['tomorrow']['text']
# assert weather['tomorrow']['low'] == 21, weather['tomorrow']['low']
# assert weather['tomorrow']['high'] == 34, weather['tomorrow']['high']

# 利用urllib读取xml
d='https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22beijing%2C%20china%22)%20and%20u%3D%27c%27%20&format=xml&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeysw%2C%20scotland%22)%20and%20u%3D%27c%27%20&format=xml&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'
weather = parse_weather(fetch_xml(d))
print('Weather:', str(weather))
