import scrapy
import time
import requests
from urllib.request import HTTPError

def base(http,ip,port):
    '''写入文件操作'''
    i = ' '
    i = i.encode()
    j = '\n'
    j = j.encode()
    filename = 'IP_POOL.text'
    f = open(filename, 'ab')
    f.write(http+i)
    f.write(ip+i)
    f.write(port+i+j)
    f.close()

class ip_pool(scrapy.Spider):
    name = 'ip'

    def start_requests(self):
        '''开始'''
        print('star'*20)
        url = ['http://www.xicidaili.com/nn/']
        for i in url:
            print(i*20)
            if i == 'http://www.xicidaili.com/nn/':
                try:
                    yield scrapy.Request(url=i,callback=self.parse_xici)
                except TimeoutError:
                    print('TimeoutError')
                except HTTPError:
                    print('HTTPError')
            #这里用if方便以后加入新的代理网站链接爬取

    def parse_xici(self,response):
        '''爬取代理，测试代理'''
        '''基于http://www.xicidaili.com/nn/'''
        full = response.xpath("//tr[@class]")
        for every,count in zip(full,range(len(full))):
            #取速度大于95的ip
            if int(every.xpath("//td[@class='country']/div/div/@style").extract()[count].split(':')[1].split('%')[0]) > 95:
                ip = every.xpath("//td[contains(text(),'.')]/text()").extract()[count]
                port = every.xpath("//td[3]/text()").extract()[count]
                http = every.xpath("//td[6]/text()").extract()[count]
                i = '{}:{}'.format(ip,port)
                #测试ip是否可用
                if int(str(requests.get('http://fanyi.youdao.com/',proxies={http:i})).split('[')[1].split(']')[0]) == 200:
                    ip = ip.encode()
                    port = port.encode()
                    http = http.encode()
                    print(ip)
                    base(http,ip,port)
        page = response.xpath("//a[contains(text(),'下一页')]/@href").extract()
        if len(page) > 0:
            page = response.urljoin(page[0])
            print(page)
            time.sleep(2)
            try:
                yield scrapy.Request(page,callback=self.parse_xici)
            except TimeoutError:
                print('TimeoutError')
            except HTTPError:
                print('HTTPError')
