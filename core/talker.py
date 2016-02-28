import json

import requests


class Talker:
    conf = None
    access_token = None

    def __init__(self, config):
        self.conf = config
        self.access_token = json.loads(requests.post(config.at_url, data=config.get_at_params()).content.decode())[
            'access_token']

    def talk(self, text):
        if (text.__len__() <= 0 or text.__len__() >= 1024):
            raise TypeError('text length error')

        return requests.post(self.conf.tk_url, data=self.conf.get_tk_params(text, self.access_token))
