'''
目标：
    自动化操作项目数据库
    判断用户是否收藏文章
    1-为收藏 0-已收藏

'''
#导包 pymysql
import pymysql

#获取连接对象
conn = pymysql.connect("127.0.0.1",
                       "root",
                       "testdatabase",
                       charset = "utf8")
#获取游标对象
#sql中所有的方法、结果都在游标对象里
cursor = conn.cursor()
#执行方法 sql
#sql查询id为1的用户是否收藏id为2的文章
sql = "select is_deleted from news_collection where user_id = 1 and article_id = 2"
cursor.execute(sql)

#获取结果并进行断言  0-收藏  fetchone
#调试结果
print(cursor.fetchone())
result = cursor.fetchone()
#断言 0 为收藏
assert 0 == result[0]


#关闭游标对象
cursor.close()
#关闭连接对象
conn.close()

'''
问题：流水线代码编写，无法复用。sql及断言方法多样
'''

