'''
目标：完成登录业务层实现
'''
#导包 unitest  ApiLogin
import unittest
from api.api_channels import ApiChannels
from parameterized import parameterized
from tools.read_json import ReadJson

#读取数据函数
def get_data():
    data = ReadJson("channel.json").read_json()
# 新建空列表，添加读取json数据
    arrs = []
    arrs.append((data.get("url"),
             data.get("mobile"),
             data.get("code"),
             data.get("headers"),
             data.get("expect_result"),
             data.get("status_code")))
    return arrs

#测试类继承unittest
class TestChannels(unittest.TestCase):

#测试方法
    # @parameterized.expand(get_data())
    def test_channels(self,url,headers,expect_result,status_code):

     # #暂时存放数据 url headers 提示，token前有前缀
     #    url = "http://ttapi.research.itcast.cn/app/v1_0/user/channels"
     #    headers = {"Content-Type":"application/json",
     #                "Authorization":"Bearer token"}

    #调用登录方法
        r = ApiChannels().api_get_channels(url,headers)
    #调试使用，后续注释
        print("查看响应结果:" , r.json())
    #断言  响应信息 状态码

        #self.assertEquals(200 , r.status_code)
        self.assertEquals(status_code, r.status_code)
        self.assertEquals(expect_result, r.json()['message'])

if __name__ == '__main__':
    unittest.main()



