'''
目标：完成登录业务层实现
'''
#导包 unitest  ApiLogin
import unittest
from api.api_login import ApiLogin
from parameterized import parameterized
from tools.read_json import ReadJson

#读取数据函数
def get_data():
    datas = ReadJson("login_more.json").read_json()
    # 新建空列表，添加读取json数据
    arrs = []
    # 使用便利获取所有value
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("mobile"),
                     data.get("code"),
                     data.get("expect_result"),
                     data.get("status_code")))
    return arrs

#测试类
class TestLogin(unittest.TestCase):

#测试方法
    @parameterized.expand(get_data())
    def test_login(self,url,mobile,code,expct_result,status_code):

    # #暂时存放数据 url mobile code
    #     url = "http://ttapi.research.itcast.cn/app/v1_0/authorizations"
    #     mobile = "13800138000"
    #     code = "123123"
    #调用登录方法
        s = ApiLogin().api_post_login(url,mobile,code)
    #调试使用，后续注释
        print("查看响应结果:" , s.json())
    #断言  响应信息 状态码
        #self.assertEquals("OK" , s.json()['message'])
        self.assertEquals(expct_result, s.json()['message'])
        #self.assertEquals(201 , s.status_code)
        self.assertEquals(status_code, s.status_code)

if __name__ == '__main__':
    unittest.main()



