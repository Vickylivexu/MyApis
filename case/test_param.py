'''
目标：回顾parameterized参数化组建
安装：pip install parameterized
使用：
    @parameterized.expant(参数)
    参数：
        单个参数：列表   eg(值1，值2)
        多个参数： 列表嵌套元组  eg[(参1值，参2值)]
    需求：输出用户名&密码，数据分别为：1. admin，123456 2.user002， 654321
'''
#导包
import unittest
from parameterized import parameterized

#建测试类
class TestPara(unittest.TestCase):
#建测试方法
    @parameterized.expand([("admin","123456"),("user002","654321")])
    def test_para(self,username,password):
        print("用户名:" ,username)
        print("密码：", password)



