from AIyuqing.aiyuqing_api import YuQingKuaiXun


class TestCorpTap:
    def setup_class(self):
        self.corptap = YuQingKuaiXun()

    def test_flash_news(self):
        r = self.corptap.flash_news()
        print(r.json().get("ok"))
        assert r.status_code == 200
        assert r.json().get("ok") == True

    def test_article_list(self):
        r = self.corptap.article_list()
        assert r.status_code == 200

    def test_article(self):
        r = self.corptap.article_list()
        id = r.json().get("id")
        r = self.corptap.article(id)
        assert r.status_code == 200

    def test_delete(self):
        r = self.corptap.create()
        id = r.json().get("id")
        r = self.corptap.delete(id)
        assert r.json() == True
        assert r.status_code == 200

    def test_create(self):
        r = self.corptap.create()
        assert r.status_code == 200
