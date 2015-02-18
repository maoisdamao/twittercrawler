__author__ = 'shinsakairi'

import time
import sys
import json
from tweepy import StreamListener
from urlthread import UrlThread


class StrListener(StreamListener):

    def __init__(self, api=None, tweets_sum=3000, data_dir="../"):
        self.api = api
        self.counter = 0
        self.tweets_sum = tweets_sum
        self.tweets_curr_sum = 0
        self.dir_input = data_dir
        self.data_dir = data_dir + '/data/' + 'twitter_data_'
        self.filename = self.data_dir + time.strftime('%Y%m%d-%H%M%S') + '.json'
        self.output = open(self.filename, 'w')
        self.threads = []

    def on_data(self, data):
        if 'in_reply_to_status' in data:
            self.on_status(data)
        elif 'warning' in data:
            warning = json.loads(data)['warnings']
            print warning('message')
            return False

    def on_status(self, status):
        self.output.write(status + "\n")
        self.counter += 1
        self.tweets_curr_sum += 1

        if self.tweets_curr_sum >= self.tweets_sum:
            self.output.close()
            thread_1 = UrlThread(self.dir_input, self.filename)
            self.threads.append(thread_1)
            thread_1.start()
            self.call_exit()
        elif self.counter >= 3000:
            self.output.close()
            thread_1 = UrlThread(self.dir_input, self.filename)
            self.threads.append(thread_1)
            self.filename = self.data_dir + time.strftime('%Y%m%d-%H%M%S') + '.json'
            self.output = open(self.filename, 'w')
            self.counter = 0
            thread_1.start()
    #    self.call_exit()

    def on_error(self, status_code):
        sys.stderr.write('Error: ' + str(status_code) + '\n')
        return False

    def on_timeout(self):
        sys.stderr.write("Timeout, sleeping for 30 seconds...\n")
        time.sleep(30)
        return

    def call_exit(self):
        for t in self.threads:
            t.join()