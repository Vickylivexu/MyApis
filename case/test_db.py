'''
目标：在unittest框架中使用数据库工具类

'''
#1.导包
import unittest
from tools.read_db import ReadDB
#2.新建测试类--继承
class TestDB(unittest.TestCase):

    #3.新建测试方法
    def test_db(self):
        #4.定义sql语句
        sql = ""
        #5.调用get_sql_one方法
        data = ReadDB().get_sql_one(sql)
        #调试 查看响应数据
        print(data)
        #6.断言
        self.assertEquals(1, data[0])


if __name__ == '__main__':
    unittest.main()


