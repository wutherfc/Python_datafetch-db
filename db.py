#!/usr/bin/python3
import pymysql

class mysqlDB():

    def __init__(self):
        try:
            self.conn = pymysql.connect(host="localhost",user="wutherfc",passwd="cyfcyf",db="testDB",cursorclass=pymysql.cursors.DictCursor)
            self.cursor = self.conn.cursor()
        except:
            print("connect failed")

    def __del__(self):
        self.conn.close()

    def DeleteAll(self, tablename):
        sql = "DELETE FROM %s WHERE 1=1"%tablename
        self.cursor.execute(sql)
        self.conn.commit()

    def CreateTable(self, tablename, attr_dict, constraint):
        sql = ""
        sql_mid = "`id` bigint(11) NOT NULL AUTO_INCREMENT,"
        for attr, value in attr_dict.items():
            sql_mid = sql_mid + "`" + attr + "`" + " " + value + ","
        sql = sql + "CREATE TABLE IF NOT EXISTS %s("%tablename
        sql = sql + sql_mid
        sql = sql + constraint
        sql = sql + ")ENGINE=InnoDB DEFAULT CHARSET=utf8;"
        print("CreateTable: "+sql)
        self.cursor.execute(sql)

    def Insert(self, tablename, attrs, values):
        values_sql = ["%s" for v in attrs]
        attrs_sql = "(" + ",".join(attrs) + ")"
        values_sql = "VALUES(" + ",".join(values_sql) + ")"

        sql = "INSERT INTO %s"%tablename
        sql = sql + attrs_sql + values_sql
        print("Insert:" + sql)
        #if data >20000?
        self.cursor.executemany(sql, values)
        self.conn.commit()

    def Select(self, tablename, con_dict=""):
        consql = ""
        if con_dict != "":
            for k, v in con_dict.items():
                consql = consql + k +"=" + v +"and"
        consql = consql + "1=1"
        sql = "SELECT * FROM %s WHERE "%tablename
        sql = sql + consql
        print("select: " + sql)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

def get_3(db, table):
    year, gdp, gdp1, gdp2, gdp3 = [], [], [], [], []
    for meta in db.Select(table):
        if "year" in meta:
            year.append(meta["year"])
        if "gdp" in meta:
            gdp.append(meta["gdp"])
        if "gdp1" in meta:
            gdp1.append(meta["gdp1"])
        if "gdp2" in meta:
            gdp2.append(meta["gdp2"])
        if "gdp3" in meta:
            gdp3.append(meta["gdp3"])
    return year, gdp, gdp1, gdp2, gdp3

def get_money_spend(db, table):
    year, total, food, cloth, house, trans, play, others = [], [], [], [], [], [], [], []
    for meta in db.Select(table):
        if "year" in meta:
            year.append(meta["year"])
        if "total" in meta:
            total.append(meta["total"])
        if "food" in meta:
            food.append(meta["food"])
        if "cloth" in meta:
            cloth.append(meta["cloth"])
        if "house" in meta:
            house.append(meta["house"])
        if "trans" in meta:
            trans.append(meta["trans"])
        if "play" in meta:
            play.append(meta["play"])
        if "others" in meta:
            others.append(meta["others"])
    return year, total, food, cloth, house, trans, play, others

"""
db = mysqlDB()
table = "test_table"
attrs = {"year": "INT NOT NULL", "gdp": "FLOAT NOT NULL"}
constraint = "PRIMARY KEY(`id`)"
db.CreateTable(table, attrs, constraint)

attrs = ["year", "gdp"]
values = [[1999, 201456.2311], [2000, 19191], [2001, 456789]]
db.Insert(table, attrs, values)

print(db.Select(table))
year=[]
gdp=[]
for meta in db.Select(table):
    if "year" in meta:
        year.append(meta["year"])
    if "gdp" in meta:
        gdp.append(meta["gdp"])

print(year)
print(gdp)
"""
