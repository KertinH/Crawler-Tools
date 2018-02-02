import requests
def detection_IP():
    '''检测ip是否可用并将可用ip生成ip池'''
    #referer可按测试网站更改
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
         'Referer':'https://www.baidu.com/link?url=zri7ohGT_WxwY7ZQtha8vMwFZzUGNd1RJOKpCdJ7HyjhNWqsULerrWwy07-CVHQ5&wd=&eqid=e15cf5ab00006ab7000000055a717610'}
    IPPOOL = []
    #读入ip文件
    with open(r'C:\Users\Administrator\PycharmProjects\IP_POOL\IP_Pool\IP_Pool\IP_POOL.text') as rd:
        all_ip = rd.read().split('\n')
    #print(all_ip)
    for one in all_ip:
        if len(one) > 0:
            #print(one)
            http = one.split(' ')[0].lower()
            ip = one.split(' ')[1]
            port = one.split(' ')[2]
            #这里的网页可以改成你想要爬取的网页
            if int(str(requests.get('http://fanyi.youdao.com/',headers=header,proxies={http:'{}://{}:{}'.format(http,ip,port)})).split('[')[1].split(']')[0]) ==200:
                p = {'ipaddr':'{}:{}'.format(ip,port)}
                IPPOOL.append(p)
    return IPPOOL
# 使用时可只取以上部分，下面两句可删去
IPPOOL = detection_IP()
print(IPPOOL)
