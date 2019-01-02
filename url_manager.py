# -*- coding: utf-8 -*-
# @Author: cyb
# url调度管理
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        """
        添加一个新链接
        :param url:
        :return:
        """
        pass

    def has_new_url(self):
        """
        还有木有待爬取得url
        :return:
        """
        pass

    def get_new_url(self):
        """
        取一个新的url准备请求他
        :return:
        """
        pass

    def add_new_urls(self,urls):
        """
        一个词条页面上所有链接添加入self.new_urls中
        :param urls:
        :return:
        """
        pass
