'''
目标：完成登录业务层实现
'''
#导包 unitest  ApiLogin
import unittest
from api.api_article import ApiArticle
from parameterized import parameterized
from tools.read_json import ReadJson

#读取数据函数
def get_data_add():
    data = ReadJson("article_add.json").read_json()
# 新建空列表，添加读取json数据
    arrs = []
    arrs.append((data.get("url"),
             data.get("headers"),
             data.get("data"),
             data.get("expect_result"),
             data.get("status_code")))
    return arrs
#获取取消收藏测试数据
def get_data_cancle():
    data = ReadJson("article_cancle.json").read_json()
    arrs = []
    arrs.append((data.get("url"),
             data.get("headers"),
             data.get("data"),
             data.get("expect_result"),
             data.get("status_code")))
    return arrs


#测试类继承unittest
class TestArticle(unittest.TestCase):

#测试方法
    @parameterized.expand(get_data_add())
    def test_collection(self,url,headers,data,expect_result,status_code):

     # #暂时存放数据 url headers 提示，token前有前缀
     #    url = "http://ttapi.research.itcast.cn/app/v1_0/user/channels"
     #    headers = {"Content-Type":"application/json",
     #                "Authorization":"Bearer token"}

    #调用收藏方法
        r = ApiArticle().api_post_collection(url,headers,data)
    #调试使用，后续注释
        print("查看响应结果:" , r.json())
    #断言  响应信息 状态码

        #self.assertEquals(200 , r.status_code)
        self.assertEquals(status_code, r.status_code)
        self.assertEquals(expect_result, r.json()['message'])

    @parameterized.expand(get_data_cancle())
    def test_delete_collection(self,url,headers,status_code):
        #调用取消收藏方法
        r = ApiArticle().api_delete_collection(url,headers)
        #调试
        print("调用取消收藏结果：" ,r.json())
        #断言响应信息
        self.assertEquals(204,r.status_code)

if __name__ == '__main__':
    unittest.main()



