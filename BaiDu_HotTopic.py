import requests
from lxml import etree


class HotTopic(object):
    def __init__(self):
        self.rt_url = 'http://top.baidu.com/buzz?b=1&c=513&fr=topbuzz_b341_c513'  # 实时热点
        self.td_url = 'http://top.baidu.com/buzz?b=341&c=513&fr=topbuzz_b1_c513'  # 今日热点
        self.wk_url = 'http://top.baidu.com/buzz?b=42&c=513&fr=topbuzz_b341_c513'  # 七日热点
        self.pl_url = 'http://top.baidu.com/buzz?b=342&c=513&fr=topbuzz_b42_c513'  # 民生热点
        self.em_url = 'http://top.baidu.com/buzz?b=344&c=513&fr=topbuzz_b342_c513'  # 娱乐热点
        self.st_url = 'http://top.baidu.com/buzz?b=11&c=513&fr=topbuzz_b344_c513'  # 体育热点
        self.header = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
        }
        self.response = self.response()

    def response(self):
        res = requests.get(url=self.rt_url, headers=self.header)  # 在这里调整url以爬取对应热点信息
        new_res = etree.HTML(res.content.decode('gbk'))
        return new_res.xpath("//*[@id='main']/div[@class='mainBody']/div/table/tr")

    def parse(self):
        for res in self.response:

            title = res.xpath("td[@class='keyword']/a[@class='list-title']/text()")
            if title != []:
                print(title[0])

            href = res.xpath("td[@class='keyword']/a[@class='list-title']/@href")
            if href != []:
                print(href[0])

            heat = res.xpath("td[@class='last']/span/text()")
            if heat != []:
                print(heat[0])
