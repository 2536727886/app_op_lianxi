from Base.base import Base
from Page.pageElements import PageElements


class SearchPage(Base):

    # 重写类方法
    def __init__(self):
        super().__init__()

    # 点击搜索按钮
    def search_test(self):
        self.click_ele(PageElements.search_btn_id)

    # 定位输入框,输入内容
    def text_test(self,text):
        self.send_ele(PageElements.search_input_id,text)

    # 结果
    def ass_test(self):
        resl = self.search_eles(PageElements.search_result_ids)
        return [i.text for i in resl]

