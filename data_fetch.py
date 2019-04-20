import time
import requests
#from pprint import *
import json


def fetch_3():
    """
    得到1999-2018年的国内生产总值及三类产业增加值
    :return: year[],gdp[]
    """
    t = time.time()
    timestamp = int(round(t * 1000))  # unix时间戳

    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
                            'AppleWebKit/537.36 (KHTML, like Gecko)' \
                            'Chrome/70.0.3538.102 Safari/537.36'
    #参数
    keyvalue = {}
    keyvalue['m'] = 'QueryData'
    keyvalue['dbcode'] = 'hgnd'
    keyvalue['rowcode'] = 'zb'
    keyvalue['colcode'] = 'sj'
    keyvalue['wds'] = '[]'
    keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":"A0201"}]'
    keyvalue['k1'] = str(timestamp)

    url = 'http://data.stats.gov.cn/easyquery.htm'
    s = requests.session()
    response = s.post(url, params=keyvalue, headers=headers)
    #print(response.text)
    #print(response.cookies.get_dict())
    #print(s.cookies)
    keyvalue['dfwds'] = '[{"wdcode":"sj","valuecode":"1999-2018"}]'
    response = s.post(url, params=keyvalue, headers=headers)
    #print(s.cookies)
   # print(response.text)
    #print(response.cookies.get_dict())

    #解析数据
    year, gdp, gdp1, gdp2, gdp3 = [], [], [], [], []
    data = json.loads(response.text)
    data_one = data['returndata']['datanodes']
    for value in data_one:
        if 'A020102' in value['code']:
            #print(value)
            year.append(int(value['code'][-4:]))
            gdp.append(float(value['data']['strdata']))
        elif 'A020103' in value['code']:
            gdp_1.append(float(value['data']['strdata']))
        elif 'A020104' in value['code']:
            gdp_2.append(float(value['data']['strdata']))
        elif 'A020105' in value['code']:
            gdp_3.append(float(value['data']['strdata']))

    print(year)
    print(gdp)
    print(gdp_1)
    print(gdp_2)
    print(gdp_3)

    return year, gdp, gdp_1, gdp_2, gdp_3

def fetch_money_spend():
    """
    得到2013-2017年居民消费情况
    :return:
    """
    t = time.time()
    timestamp = int(round(t * 1000))  # unix时间戳

    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
                            'AppleWebKit/537.36 (KHTML, like Gecko)' \
                            'Chrome/70.0.3538.102 Safari/537.36'
    # 参数
    keyvalue = {}
    keyvalue['m'] = 'QueryData'
    keyvalue['dbcode'] = 'hgnd'
    keyvalue['rowcode'] = 'zb'
    keyvalue['colcode'] = 'sj'
    keyvalue['wds'] = '[]'
    keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":"A0A02"}, {"wdcode":"sj","valuecode":"2013-2017"}]'
    keyvalue['k1'] = str(timestamp)

    url = 'http://data.stats.gov.cn/easyquery.htm'
    s = requests.session()
    response = s.post(url, params=keyvalue, headers=headers, allow_redirects=False)

    #print(response.text)
    #print(response.status_code)
    # 解析数据

    year = []
    total = [] #人均消费支出
    food = [] #食物
    cloth = [] #衣服
    house = [] #住房
    trans = [] #交通通信
    play = [] #玩
    others = []

    data = json.loads(response.text)
    data_one = data['returndata']['datanodes']
    for value in data_one:
        if 'A0A0206' in value['code']:
            #print(value)
            year.append(int(value['code'][-4:]))
            total.append(float(value['data']['strdata']))
        elif 'A0A0207' in value['code']:
            food.append(float(value['data']['strdata']))
        elif 'A0A0208' in value['code']:
            cloth.append(float(value['data']['strdata']))
        elif 'A0A0209' in value['code']:
            house.append(float(value['data']['strdata']))
        elif 'A0A020B' in value['code']:
            trans.append(float(value['data']['strdata']))
        elif 'A0A020C' in value['code']:
            play.append(float(value['data']['strdata']))

    print(year)
    print(total)
    print(food)
    print(cloth)
    print(house)
    print(trans)
    print(play)
    for i in range(0, 5):
        others.append(total[i] - food[i] - cloth[i] - house[i] - trans[i] - play[i])

    return year, total, food, cloth, house, trans, play, others


