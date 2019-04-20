from db import mysqlDB, get_3, get_money_spend
from data_fetch import fetch_3, fetch_money_spend
from figure_plot import draw_3_1, draw_pie_charts, draw_line, draw_3_2

table1 = "task1"
table2 = "task2"

if __name__ == '__main__':
    db = mysqlDB()
    #建立Table
    attrs1 = {"year": " INT NOT NULL", "gdp": "FLOAT NOT NULL",
              "gdp1": "FLOAT NOT NULL", "gdp2": "FLOAT NOT NULL", "gdp3": "FLOAT NOT NULL"}

    attrs2 = {"year": "INT NOT NULL", "total": "FLOAT NOT NULL",
              "food": "FLOAT NOT NULL", "cloth": "FLOAT NOT NULL","house": "FLOAT NOT NULL",
              "trans":"FLOAT NOT NULL", "play": "FLOAT NOT NULL", "others": "FLOAT NOT NULL"}

    constraint = "PRIMARY KEY(`id`)"
    db.CreateTable(table1, attrs1, constraint)
    db.CreateTable(table2, attrs2, constraint)

    #获取数据并存入数据库
    insert_attrs1 = ["year", "gdp", "gdp1", "gdp2", "gdp3"]
    year, gdp, gdp1, gdp2, gdp3 = fetch_3()
    insert_values1 = list(zip(year, gdp, gdp1, gdp2, gdp3))
    db.Insert(table1, insert_attrs1, insert_values1)

    insert_attrs2 = ["year", "total", "food", "cloth", "house", "trans", "play", "others"]
    year, total, food, cloth, house, trans, play ,others = fetch_money_spend()
    insert_values2 = list(zip(year, total, food, cloth, house, trans, play ,others))
    db.Insert(table2, insert_attrs2, insert_values2)

    #读取数据并画图
    #task1
    year, gdp, gdp1, gdp2, gdp3 = get_3(db, table1)
    draw_3_1(year, gdp)
    draw_3_2(year, gdp1, gdp2, gdp3)
    #task2
    year, total, food, cloth, house, trans, play ,others = get_money_spend(db, table2)
    draw_pie_charts(food, cloth, house, trans, play, others)
    draw_line(year, total)

    #清除数据
    db.Deleteall(table1)
    db.DeleteAll(table2)
