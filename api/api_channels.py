'''
目标：实现登录接口对象封装
'''
#导入 requests
import requests

#类  登录接口对象
class ApiChannels(object):
    #新建测试方法


#方法：获取用户频道方法
    def api_get_channels(self,url,headers):

    #调用get请求
        return requests.get(url, headers = headers)


