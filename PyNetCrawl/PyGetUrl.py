# This Python file uses the following encoding: utf-8
#class netdata get

#获取所有网页链接
import re
import urlparse
import urllib2
import time
from datetime import datetime
import robotparser
import Queue

print('>>>>>>>>>>>>>>>>>>>>>>>>>>抓取网页链接函数')
def link_crawler(seed_url, link_regex=None, delay=5, max_depth=-1, max_urls=-1, headers=None, user_agent='long', proxy=None, num_retries=1):
    """"Crawl from the given seed URL following links matched by link_regex"""
    #待爬取得网址队列
    crawl_queue = Queue.deque([seed_url])
    #已被查看的网址的深度
    seen = {seed_url : 0}
    #跟踪查看有多少被下载的网址
    num_urls = 0
    rp = get_robots(seed_url)
    throttle = Throttle(delay)
    headers = headers or {}
    if user_agent:
        url = crawl_queue.pop()
    while crawl_queue:
        url = crawl_queue
        #检查URL是否通过robots.txt限制
        if rp.can_fetch(user_agent, url):
            throttle.wait(url)
            html = download(url, headers, proxy=proxy, num_retries=num_retries)
            links = []
            depth = seen[url]
            if depth != max_depth:
                #可以爬更远
                if link_regex:
                    # 用于匹配正则表达式的链接的筛选器
                    links.extend(link for link in get_links(html) if re.match(link_regex, link))
                for link in links:
                    link = normalize(seed_url, link)
                    # 验证是否已经被爬过
                    if link not in seen:
                        seen[link] = depth + 1
                        # 检查链接在同一域内
                        if same_domain(seed_url, link):
                            #如果成功就加入队列
                            crawl_queue.append(link)
            #检查是否已达到下载的最大值
            num_urls += 1
            if num_urls == max_urls:
                break
        else:
            print 'Blocked by robots.txt:', url

print(">>>>>>>>>>>>>>>>>>>>>>>>>>通过在同一域请求之间睡眠来下载加阀")
class Throttle:
    """Throttle downloading by sleeping between requests to same domain
    """

    def __init__(self, delay):
        # amount of delay between downloads for each domain
        self.delay = delay
        # timestamp of when a domain was last accessed
        self.domains = {}

    def wait(self, url):
        domain = urlparse.urlparse(url).netloc
        last_accessed = self.domains.get(domain)

        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.now() - last_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        self.domains[domain] = datetime.now()


print(">>>>>>>>>>>>>>>>>>>>>>>>>>下载网页内容")
def download(url, headers, proxy, num_retries, data=None):
    print 'Downloading:', url
    request = urllib2.Request(url, data, headers)
    opener = urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        response = opener.open(request)
        html = response.read()
        code = response.code
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = ''
        if hasattr(e, 'code'):
            code = e.code
            if num_retries > 0 and 500 <= code < 600:
                # retry 5XX HTTP errors
                return download(url, headers, proxy, num_retries-1, data)
        else:
            code = None
    return html


print(">>>>>>>>>>>>>>>>>>>>>>>>>>通过删除哈希和添加域来正常化此URL")
def normalize(seed_url, link):
    """Normalize this URL by removing hash and adding domain
    """
    link, _ = urlparse.urldefrag(link)  # remove hash to avoid duplicates
    return urlparse.urljoin(seed_url, link)

print(">>>>>>>>>>>>>>>>>>>>>>>>>>返回正确的网址如果两个网址属于同一个域")
def same_domain(url1, url2):
    """Return True if both URL's belong to same domain
    """
    return urlparse.urlparse(url1).netloc == urlparse.urlparse(url2).netloc

print(">>>>>>>>>>>>>>>>>>>>>>>>>>为当前域初始化robot文件解析初始化")
def get_robots(url):
    """Initialize robots parser for this domain
    """
    rp = robotparser.RobotFileParser()
    rp.set_url(urlparse.urljoin(url, '/robots.txt'))
    rp.read()
    return rp

print(">>>>>>>>>>>>>>>>>>>>>>>>>>获取网址")
def get_links(html):
    """Return a list of links from html
    """
    # a regular expression to extract all links from the webpage
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # list of all links from the webpage
    return webpage_regex.findall(html)

#主函数
print("主函数")
if __name__ == '__main__':
    link_crawler('http://example.webscraping.com', '/(index|view)', 0, 1, 'BadCrawler')
    link_crawler('http://example.webscraping.com', '/(index|view)', 0, 1, 1, 'GoodCrawler')