from AIyuqing.baseapi import BaseApi001


class YuQingKuaiXun(BaseApi001):
    url = 'http://123.56.138.96:3012/api/'

    # 舆情快讯
    def create(self):
        data = {
            "method": "post",
            "url": self.url + 'ainews-user/company-group/create',
            "headers": {"Content-Type": "application/json;charset=utf-8", "Authorization": self.token},
            "json": {"name": "mmm"}
        }

        return self.send(data)

    def flash_news(self):
        data = {
            "method": "post",
            "url": self.url + "ainews-espy/api/opinion/flash-news",
            "headers": {
                "Content-Type": "application/json;charset=utf-8", "Authorization": self.token
            },
            "json": {
                "start_time": "2021-10-20T16:56:47", "end_time": "2021-10-27T16:56:47", "page": 1, "pagesize": 20
            },
        }
        return self.send(data)

    def article_list(self):
        data = {
            "method": "post",
            "url": self.url + "ainews-espy/api/opinion/v2/article-list",
            "headers": {
                "Content-Type": "application/json;charset=utf-8", "Authorization": self.token
            },
            "json": {
                "sort_by": "pub_time", "sort_order": "desc", "page": 1, "board": "all", "classification": ""
                , "category_key": "", "cp_type": "all", "article_type": "all", "risk_level": [0, 1, 2],
                "start_time": "2021-10-24T00:00:00",
                "end_time": "2021-10-30T19:14:01"
            },
        }
        print(self.send(data).json())
        return self.send(data)

    def article(self, id):
        data = {
            "method": "post",
            "url": self.url + "ainews-espy/api/company/article",
            "headers": {
                "Content-Type": "application/json;charset=utf-8", "Authorization": self.token
            },
            "json": {
                "cp_code": ["undefined"], "id": id
            },
        }
        return self.send(data)

    def delete(self, id):
        data = {
            "method": "get",
            "url": self.url + "ainews-user/company-group/delete",
            "headers": {"Content-Type": "application/json;charset=utf-8", "Authorization": self.token},
            "params": {"id": id}
        }
        print("parmas")
        return self.send(data)


a = YuQingKuaiXun().article_list().json().get("data")[0]["id"]
print(YuQingKuaiXun().article(a).json())
b = YuQingKuaiXun().create().json().get("id")
print(YuQingKuaiXun().delete(b))
# def d():
#     _url4= 'http://123.56.138.96:3012/api/ainews-espy/api/opinion/v2/article-list'
#     _headers4 = {"Content-Type": "application/json;charset=utf-8","Authorization":get_token()}
#     _data4 = {"sort_by":"pub_time","sort_order":"desc","page":1,"board":"all","classification":""
#     ,"category_key":"","cp_type":"all","article_type":"all","risk_level":[0,1,2],"start_time":"2021-10-24T00:00:00",
#     "end_time":"2021-10-30T19:14:01"}
#     r5 = requests.request(method='post',url=_url4,headers=_headers4,json=_data4)
#     print(json.dumps(r5.json(),indent = 2,ensure_ascii=False))
#     return r5.json()["data"][0]["id"]
# def e():
#     _url5='http://123.56.138.96:3012/api/ainews-espy/api/company/article'
#     _headers5 = {"Content-Type": "application/json;charset=utf-8","Authorization":get_token()}
#     _data5 ={"cp_code":["undefined"],"id":d()}
#     r6 = requests.request(method='post',url=_url5,headers=_headers5,json=_data5)
#     print(json.dumps(r6.json(), indent=2, ensure_ascii=False))
