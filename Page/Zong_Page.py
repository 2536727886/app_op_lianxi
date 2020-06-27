

# 入口设置
from Page.searchPage import SearchPage


class ZongPage:

    """返回页面搜索结果类"""
    @classmethod
    def search(cls):
        return SearchPage()