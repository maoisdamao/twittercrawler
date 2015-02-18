__author__ = 'shinsakairi'

import threading

from parse import UrlExtractor


class UrlThread(threading.Thread):

    def __init__(self, path_dir, filename):
        threading.Thread.__init__(self)
        self.path_dir = path_dir
        self.filename = filename

    # run() will be called auto when thread created
    def start(self):
        u = UrlExtractor(self.path_dir, self.filename)
        u.url_download()