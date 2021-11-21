import datetime
import json

import requests


class DingRobot:
    def __init__(self):
        self.allure = "http://mcm:mcm.521520.@47.94.5.28:9000/job/aiyuqing/allure/widgets/suites.json"
        self.ding = "https://oapi.dingtalk.com/robot/send?access_token=4047968f7f40495a86e51b1b4a8eb16a9fc806a005fb670a6476678d164661e7"
        self.error = self.get_allure()

    def get_allure(self):
        jenkins_data = requests.get(self.allure).json()
        case_error = jenkins_data["items"][0]["statistic"]["failed"]
        return case_error

    def send_report(self):
        if self.error > 0:
            headers = {"Content-Type": "application/json;charset=utf-8"}
            content = {
                "msgtype": "link",
                "link": {
                    "text": "账号mcm,密码mcm.521520.",
                    "title": "002" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "picUrl": "",
                    "messageUrl": "http://mcm:mcm.521520.@47.94.5.28:9000/job/aiyuqing/allure"
                }
            }
            requests.post(self.ding, headers=headers, data=json.dumps(content))
        else:
            print('无报错')

if __name__ == '__main__':
    DingRobot().send_report()

