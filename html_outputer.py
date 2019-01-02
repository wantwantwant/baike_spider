# -*- coding: utf-8 -*-
# @Author: cyb
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []     # 类里面的全局变量，先存一个数据备份，供output等函数使用

    def collect_data(self, new_url, new_data):
        assert new_url is not None
        assert  new_data is not None

        self.datas.append((new_url, new_data))



    def output_html(self):
        """
        输出到output.html
        :return:
        """
        file = open('output.html', mode='w')
        # 从例子可以看出djano的模板来渲染语言原理
        file.write("<html>")
        file.write("<body>")

        for row in self.datas:
            file.write("<tr style='border:1px;'>")
            file.write(f"<td>{row[0]}</td>")
            file.write(f"<td>{row[1]['title']}</td>")
            file.write(f"<td>{row[1]['summary']}</td>")

            file.write("</tr>")
        file.write("</body>")
        file.write("</html>")

    def save_db(self):
        """保存到数据库"""
        pass
