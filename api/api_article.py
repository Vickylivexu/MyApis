'''
目标：实现文章接口对象封装
'''
#导入 requests
import requests

#类  文章收藏
class ApiArticle(object):
    #新建测试方法


#方法：新建收藏文章的方法(headers内存在鉴权文件)
    def api_post_collection(self,url, headers,data):
    #调用post方法  返回响应对象
        return requests.post(url,headers = headers ,json = data)

#新建取消收藏文章的方法

    #调用delete方法，返回响应对象
    def api_delete_collection(self,url,headers):

    #调用get请求
        return requests.delete(url,headers)




