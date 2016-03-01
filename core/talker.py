import json

import requests

from core.sentence import Sentence


# 一个讲述人
class Talker:
    conf = None
    access_token = None

    def __init__(self, config):
        self.conf = config
        self.access_token = json.loads(requests.post(config.at_url, data=config.get_at_params()).content.decode())[
            'access_token']

    # 讲话
    def talk(self, text):
        if (text.__len__() <= 0 or text.__len__() >= 1024):
            raise TypeError('text length error')

        return Sentence(text, requests.post(self.conf.tk_url, data=self.conf.get_tk_params(text, self.access_token)))
