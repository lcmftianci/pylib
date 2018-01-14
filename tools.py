__author__ = 'CULA'

#utf-8

import re

#处理页面标签
class Tools:
    #去除img标签，1-7位空格
    removeImg = re.compile('<img.*?>|{ 1,7}|')

    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')

    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')

    # 将表格制表<td>替换为\t
    replaceTD = re.compile('<td>')

    #将换行符双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')

    #其余标签删除
    removeExtraTag = re.compile('<.*?>')

    #将多行空行删除
    removeNoneLine = re.compile('\n+')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        x = re.sub(self.removeNoneLine, "\n", x)
        return x.strip()