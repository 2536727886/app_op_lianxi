

# 测试类，对搜索的结果返回
import pytest

from Base.driver import Driver
from Page.Zong_Page import ZongPage


class TestSearch:

    def teardown_class(self):
        # 退出
        Driver.quit_app_driver()

    # 依赖方法，点击搜索，只需要点击一次，利用fixture的类方法
    @pytest.fixture(scope="class", autouse=True)
    def click_btn(self):
        ZongPage.search().search_test()

    # 输入内容，返回结果
    @pytest.mark.parametrize("search_data, exp_data", [("1", "休眠"), ("i", "IP地址"), ("m", "MAC地址")])
    def test_text(self, search_data, exp_data):
        # 输入内容
        ZongPage.search().text_test(search_data)
        # 获取结果
        resl = ZongPage.search().ass_test()
        # 断言
        assert exp_data in resl