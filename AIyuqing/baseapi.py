import json

import requests


class BaseApi001:
    def __init__(self):
        self.token = self.get_token()

    def send(self, kwargs):
        r = requests.request(**kwargs)
        # print(json.dumps(r.json(), indent=1, ensure_ascii=False))
        return r

    def get_token(self):
        data = {
            "url": 'http://123.56.138.96:3012/api/ainews-user/user/login',
            "method": "post",
            "headers": {"Content-Type": "application/json;charset=utf-8"},
            "json": {"name": "lsj1", "password": "123123"},
        }
        token = self.send(data).json()["access_token"]
        return token
