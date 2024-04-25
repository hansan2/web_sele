# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/14 15:27
# @Author  : JW
# @FileName: test_index.py
"""
import unittest
from selenium import webdriver
import time
import ddt

from page_objects.login_page import LoginPage
from page_objects.index_page import IndexPage
from page_objects.vip_index_page import VipIndexPage
from test_datas.login_datas import *
from test_datas.index_datas import AddShop as AS, JumpVipBackground as JVB


@ddt.ddt
class TestIndex(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.login_page = LoginPage(self.driver)
        self.index_page = IndexPage(self.driver)
        self.vip_index_page = VipIndexPage(self.driver)
        self.driver.get("http://admin-jk8.kdwaimai.com")
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()
        pass

    def test_jump_vip_background(self):
        self.login_page.user_login(username=login_pass["username"], password=login_pass["password"])
        time.sleep(0.5)
        # self.assertIn(login_pass["check"], IndexPage(self.driver).user_name_check())
        cur_handles = self.driver.window_handles
        self.index_page.jump_vip_background()
        self.index_page.switch_window(cur_handles)
        time.sleep(0.5)
        self.assertEqual(JVB.jump_vip_background_pass["check"], self.vip_index_page.vip_background_check.text)
        # 调用添加会员卡点击事件
        # self.vip_index_page.add_vip_card_click
        # time.sleep(3)

    def test_add_shop(self):
        self.login_page.user_login(username=login_pass["username"], password=login_pass["password"])
        self.index_page.get_shop_management.click()
        self.index_page.get_pass_shop.click()
        self.index_page.add_shop()
        time.sleep(0.2)
        self.index_page.add_shop_input_information(shop_name=AS.add_shop_pass["shop_name"],
                                                   shop_detailed_address=AS.add_shop_pass["shop_detailed_address"],
                                                   social_credit_code=AS.add_shop_pass["social_credit_code"],
                                                   near=AS.add_shop_pass["near"])
        time.sleep(1)
        self.index_page.add_shop_input_information_2()
        time.sleep(1)
        self.assertEqual(AS.add_shop_pass["check"], self.index_page.add_shop_check.text)

    # @ddt.data(*AS.add_shop_fail)
    # def test_add_shop_fail(self, data):
    #     self.login_page.user_login(username=login_pass["username"], password=login_pass["password"])
    #     self.index_page.get_shop_management.click()
    #     self.index_page.get_pass_shop.click()
    #     self.index_page.add_shop()
    #     time.sleep(0.2)
    #     self.index_page.add_shop_input_information(shop_name=data["shop_name"],
    #                                                shop_detailed_address=data["shop_detailed_address"],
    #                                                social_credit_code=data["social_credit_code"],
    #                                                near=data["near"])
    #     time.sleep(1)


if __name__ == '__main__':
    unittest.main()
