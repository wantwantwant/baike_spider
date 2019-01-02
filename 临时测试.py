# -*- coding: utf-8 -*-
# @Author: cyb

from html_downloader import HtmlDownloader

downloader = HtmlDownloader()
html_content = downloader.download(url='https://baike.baidu.com/item/Python/407313')
print(html_content)

# 测试得到响应的htmlcontent，经过比对是纯静态页面，想要的数据都已包含。
# # resp.text自动转换偶尔会得到乱码，所以改为resp.content.decode()