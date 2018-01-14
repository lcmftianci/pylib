# This Python file uses the following encoding: utf-8
import re
import urllib
import urllib2
import xlwt
from bs4 import BeautifulSoup
import lxml.html
from datetime import datetime


#下载网站内容
def download(url):
    print 'DownLoading', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'DownLoad error:', e.reason
        html = None
    return html

#将网站内容解析，解析出网站中存储的所有网页链接
def splithtml(html):
    print html
    return html

#写入文件
def filefrite(ncode):
    print ncode

#读取文件
def fileread(ncode, filepath):
    print ncode
    for i in open(filepath):
        print i
    with open(filepath) as f:
        f.readlines()#   将文件内容以列表的形式存放
        f.close()

    f = open(filepath)
    f.readline()
    f.close()
    return

#实现switch case语句,类似于下面
# function(argument){
#     switch(argument) {
#         case 0:
#             return "zero";
#         case 1:
#             return "one";
#         case 2:
#             return "two";
#         default:
#             return "nothing";
#     };
# };
def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return switcher.get(argument, "nothing")




#测试读写excel文件
def testxlwt():
    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
                         num_format_str='#,##0.00')
    style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')

    ws.write(0, 0, 1234.56, style0)
    ws.write(1, 0, datetime.now(), style1)
    ws.write(2, 0, 1)
    ws.write(2, 1, 1)
    ws.write(2, 2, xlwt.Formula("A3+B3"))

    wb.save('example.xls')





with open("E:\\opensource\\code\\tmlf.txt", "w") as f:
    b = open("E:\\opensource\\code\\htmlb.txt", "w")
    b.write(download("http://m.csdn.net/article/2014-11-21/2822753-material-design-libs"))
    res_tr = r'<a href="https://github.com/(.*?)" itemprop="name codeRepository">'
    m_num = [1,2,3,4,5,6,7,8]
    for each in m_num:
        list1 = []
        print each
        # if each == 0:
        #     htmlPath = "https://github.com/googlesamples"
        #     list1.append(htmlPath)
        # else:
        htmlPath = "https://github.com/" + str(each)
        list1.append(htmlPath)

        for listatr in list1:
            print listatr
            m_str = re.findall(res_tr, download(str(listatr)), re.S | re.M)
            for line in m_str:
                # new_line = line.split('<')[1]
                # print new_line
                # print line
                #strline = line + "  \n"
                #合成想要的字符串用于下载文件
                strHtml = "git " + "clone " + "https://github.com/" + line + "\n"
                f.write(strHtml)


    # m_str = re.findall(res_tr, download("https://github.com/googlesamples"), re.S|re.M)
    # for line in m_str:
    #     #new_line = line.split('<')[1]
    #     #print new_line
    #     #print line
    #     f.write(line)
    f.close()
    b.close()
    print 'hello world'