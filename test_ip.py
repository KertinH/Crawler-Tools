import requests
def detection_IP():
    '''检测ip是否可用并将可用ip生成ip池'''
    #referer可按测试网站更改
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
         'Connection': 'keep-alive'}
    IPPOOL = []
    local_ip = '42.48.200.188'
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
            try:
                #这个网页会直接返回当前ip
                res = requests.get('http://icanhazip.com/',headers=header,proxies={'http':'http://{}:{}'.format(ip,port)},timeout=1)
                if res.status_code ==200:
                    if res.text != local_ip:
                        p = {'ipaddr':'{}:{}'.format(ip,port)}
                        IPPOOL.append(p)
            except:
                pass
    return IPPOOL
IPPOOL = detection_IP()
# 使用时可只取以上部分
print(IPPOOL)
