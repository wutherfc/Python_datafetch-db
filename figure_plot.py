from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


def draw_3_1(year, gdp):
    #解决中文显示问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    #year, gdp, gdp_1, gdp_2, gdp_3 = fetch_3()
    fig, ax = plt.subplots()
    ax.plot(year, gdp, linewidth=3, color='c', marker='o', markerfacecolor='b', markersize=5)
    ax.set(xlabel='年份', ylabel='国内生产总值(亿元)')
    ax.set_title('1999-2018年国内生产总值变化(亿元)')
    tick_spacing = 2
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    #plt.xticks(year, group_lables, rotation=0)
    plt.savefig("3_1.png")
    plt.grid()
    plt.show()

def draw_3_2(year, gdp_1, gdp_2, gdp_3):
    #解决中文显示问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    #year, gdp, gdp_1, gdp_2, gdp_3 = fetch_3()
    year = list(reversed(year[0:10:1]))
    gdp_1 = list(reversed(gdp_1[0:10:1]))
    gdp_2 = list(reversed(gdp_2[0:10:1]))
    gdp_3 = list(reversed(gdp_3[0:10:1]))

    ind = np.arange(10)

    width = 0.35

    p1 = plt.bar(ind, gdp_1, width)
    p2 = plt.bar(ind, gdp_2, width, bottom=gdp_1)
    p3 = plt.bar(ind, gdp_3, width, bottom=gdp_2)

    plt.ylabel('产业增加值(亿元)')
    plt.xticks(ind, year)
    plt.title('2009-2018年中国三类产业增加值(亿元)')
    plt.legend((p1[0], p2[0], p3[0]), ('第一产业', '第二产业', '第三产业',))
    plt.savefig("3_2.png")
    plt.show()

#pie charts
def draw_pie_charts(food, cloth, house, trans, play, others):
    #解决中文显示问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    #year, total, food, cloth, house, trans, play, others = fetch_money_spend()
    labels = ['食品烟酒', '衣着', '居住', '交通和通信', '教育，文化和娱乐', '其他']
    sizes = [food[0], cloth[0], house[0], trans[0], play[0], others[0]]
    explode = (0.1, 0.1, 0, 0, 0, 0)
    fig1, ax1 = plt.subplots()
    ax1.set_title('2017年中国居民人均消费各项占比')
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig("pie.png")
    plt.show()

def draw_line(year, total):
    #解决中文显示问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    #year, total, food, cloth, house, trans, play, others = fetch_money_spend()
    fig, ax = plt.subplots()
    group_lables = ['2017年', '2016年', '2015年', '2014年', '2013年']
    ax.plot(year, total, linewidth=3, color='c', marker='o', markerfacecolor='b', markersize=10)
    ax.set(xlabel='年份', ylabel='居民人均消费支出(元)')
    ax.set_title('2013-2017年中国居民人均消费支出(元)')
    plt.xticks(year, group_lables, rotation=0)
    #plt.grid()
    for a, b in zip(year, total):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

    plt.savefig("line.png")
    plt.show()
"""
draw_line()
draw_pie_charts()
draw_3_2()
draw_3_1()
"""