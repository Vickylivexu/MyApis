#导入json包
import json

#打开json文件并获取文件流
# with open("../data/login.json" , "r" , encoding="utf-8") as f:
# #调用load方法加载文件流
#     data = json.load(f)
#     print("获取的数据为： ", data)
'''
问题：
    1。未封装无法在别的模块使用
    故需要封装
'''
# def read_json():
#     with open("../data/login.json" , "r" , encoding="utf-8") as f:
#         return json.load(f)
'''
问题：
    2。数据存储文件有好几个，如果写死在读取别的文件无法使用
    使用参数替换写死的文件名
'''
#使用参数替换静态文件名
class ReadJson(object):
    def __init__(self, filename):
        self.filepath = "../data/" + filename
    def read_json(self):
        with open(self.filepath , "r" , encoding="utf-8") as f:
            return json.load(f)

# if __name__ == '__main__':
#     print(ReadJson("login.json").read_json())
'''
问题：
    3.预期格式为列表嵌套元组[(),()]但返回字典类型？
    --读取字典内容，并添加到列表中
'''

if __name__ == '__main__':
    #print(ReadJson("login.json").read_json())
    # #登录数据调试
    # data = ReadJson("login.json").read_json()
    # #新建空列表，添加读取json数据
    # arrs = []
    # arrs.append((data.get("url"),
    #              data.get("mobile"),
    #              data.get("code"),
    #              data.get("expect_result"),
    #              data.get("status_code")))
    # print(arrs)

    #获取channels调试
    data = ReadJson("channel.json").read_json()
    #新建空列表，添加读取json数据
    arrs = []
    arrs.append((data.get("url"),
                 data.get("mobile"),
                 data.get("code"),
                 data.get("data"),
                 data.get("headers"),
                 data.get("expect_result"),
                 data.get("status_code")))
    print(arrs)