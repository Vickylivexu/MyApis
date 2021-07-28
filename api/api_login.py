'''
目标：实现登录接口对象封装
'''
#导入 requests
import requests

#类  登录接口对象
class ApiLogin(object):

#方法：登录方法
    def api_post_login(self,url, mobile, code):
    #headers定义
        headers = {"Content-Type": "application/json"}
    #data定义
        data = {"mobile": mobile, "code": code}
    #调用post并返回响应对象
        return requests.post(url, headers = headers, json=data)

    '''
    提示：url、mobile、code都需要通过参数化形式传递，所以在函数内使用动态传参
    '''
