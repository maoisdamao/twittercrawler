__author__ = 'shinsakairi'

import json
import re
import urllib2, socket
import time

tweets_data_path = 'data/twitter_data_20150208-010846.json'


class UrlExtractor:

    def __init__(self, data_path, file_name):
        self.tweets_data_path = data_path
        self.tweets_file = open(file_name, "r")

    def url_download(self):
        for line in self.tweets_file:
            try:
                tweets = json.loads(line)
                tweet = tweets['text']
                tweets_link = self.extract_link(tweet)
                if tweets_link != '':
                    #print tweets['id_str'] + '\t' + tweets_link
                    content = urllib2.urlopen(tweets_link).read()
                    socket.setdefaulttimeout(5)
                    #print content.url
                    filename = self.tweets_data_path + '/html/' + tweets['id_str'] \
                                 + time.strftime('%Y%m%d-%H%M%S') + '.html'
                    if content:
                        output = open(filename, 'w')
                        output.write(content)
                        output.close()
                    else:
                        continue
            except:
                continue
        return True

    def extract_link(self, text):
        regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
        match = re.search(regex, text)
        if match:
            return match.group()
        return ''