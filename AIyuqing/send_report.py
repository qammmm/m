import datetime
import json

import requests


class DingRobot:
    def __init__(self):
        self.allure = "http://mcm:mcm.521520.@47.94.5.28:9000/job/aiyuqing/allure/widgets/suites.json"
        self.ding = 'https://oapi.dingtalk.com/robot/send?access_token=' \
                    'ca6944d0d31cc88634a4b250e02d97ab3b94c48660bf7e82b0f809351a56cded'
        self.error = self.get_allure()

    def get_allure(self):
        jenkins_data = requests.get(self.allure).json()
        case_error = jenkins_data["items"][0]["statistic"]["failed"]
        return case_error

    def send_report(self):
        if self.error == 0:
            headers = {"Content-Type": "application/json;charset=utf-8"}
            content = {
                "msgtype": "text",
                "text": {
                    "text": "账号mcm,密码mcm.521520.",
                    "title": "田继洋" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "picUrl": "",
                    "messageUrl": "http://mcm:mcm.521520.@47.94.5.28:9000/job/aiyuqing/allure"
                }
            }
            response = requests.post(self.ding, headers=headers, data=json.dumps(content))
        else:
            print('无报错')


if __name__ == '__main__':
    DingRobot().send_report()
