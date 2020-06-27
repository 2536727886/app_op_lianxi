import allure


class TestAllureStepP:
    @allure.severity(allure.severity_level.BLOCKER) # 对用例进行划分，最重要
    @allure.step("我是步骤名称")
    def test_001(self):
        """添加测试步骤"""
        # 附件，以及内容
        allure.attach("我是附件的内容。", "附件名字")

    @allure.severity(allure.severity_level.CRITICAL) # 比较重要
    def test_002(self):
        assert False

    @allure.severity(allure.severity_level.NORMAL) # 正常用例
    def test_003(self):
        assert True

    @allure.severity(allure.severity_level.MINOR) # 不重要用例
    def test_004(self):
        assert True

    @allure.severity(allure.severity_level.TRIVIAL) # 可以忽略的用例
    def test_005(self):
        assert True
