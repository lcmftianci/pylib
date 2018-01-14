import urllib
import urllib.request
import re

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    image = re.compile(reg)
    html = html.decode('UTF-8')
    unicode(html, errors='ignore')
    imglist = re.findall(image,html)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, 'D:\E\%s.jpg' % x)
        x+=1
html = getHtml("http://tieba.baidu.com/p/xxxx")
getImg(html)