import re

import pymongo
from pymongo import MongoClient
# 链接mongo服务器
mong = MongoClient()
# 链接指定数据库
db = mong.bj1909

# db.student.insert({'name':'大坏蛋','age':30})

data1 = db.student.find({"name":re.compile("坏")})
print(list(data1))

# data = db.student.find({'name':{"$regex":'坏'}})
# print(list(data))

# data = db.student.find()
# for i in data:
#     print(i)



mong.close()