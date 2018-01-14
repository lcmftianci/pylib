import urllib.request

def download(url):
    print('Downloading:', url)
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.request._ftperrors as e:
        print('Download error', e.reason())
        html = None
    return html


download('https://github.com/lcmftianci/RecyclerViewDemo.git')


class spider:
    sp = 0
    def __init__(self):
        self.sp = 12

    def split(self, s, n):
        print('my name is', s, n)

    def splitNi(self, ss, nn, ll):
        self.split(self, ss,nn)
        print("your name is", ss, nn, ll)

mSpider = spider
mSpider.split(mSpider, 's', 'b')
mSpider.splitNi(mSpider, 's','b','a')

import re
import urllib.request

# ------ 获取网页源代码的方法 ---
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

# ------ getHtml()内输入任意帖子的URL ------
html = getHtml("http://tieba.baidu.com/p/2738151262")
# ------ 修改html对象内的字符编码为UTF-8 ------
html = html.decode('UTF-8')

# ------ 获取帖子内所有图片地址的方法 ------
def getImg(html):
    # ------ 利用正则表达式匹配网页内容找到图片地址 ------
    reg = r'src="([.*\S]*\.jpg)" pic_ext="jpeg"'
    imgre = re.compile(reg);
    imglist = re.findall(imgre, html)
    return imglist

imgList = getImg(html)
imgName = 0
for imgPath in imgList:
    # ------ 这里最好使用异常处理及多线程编程方式 ------
    f = open("D:/picture/"+str(imgName)+".jpg", 'wb')
    print('pic :',imgPath)
    f.write((urllib.request.urlopen(imgPath)).read())
    f.close()
    imgName += 1

print("All Done!")

#python3.4 爬虫教程
#爬取网站上的图片
#林炳文Evankaka(博客：http://blog.csdn.net/evankaka/)

