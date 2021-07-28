'''
目标：完成数据库工具类封装
分析：
    1.主要方法
        def get_sql_one(sql)
    2.辅助方法
        获取连接对象
        获取游标对象
        关闭游标对象
        关闭连接对象
'''

#导包 pymysql
import pymysql

#新建数据库工具类
class ReadDB:
    #定义连接对象  类方法
    conn = None
    #定义
# 辅助方法封装
    #获取连接对象
    def get_conn(self):
        if self.conn is None:
            self.conn = pymysql.connect("127.0.0.1",
                                        "root",
                                        "testdatabase",
                                        charset = "utf8")
        #返回连接对象
        return self.conn

    #获取游标对象
    def get_cursor(self):
        return self.get_conn().cursor()
    #关闭游标对象
    def close_cursor(self,cursor):
        if cursor:
            cursor.close()

    #关闭连接对象
    def close_conn(self):
        if self.conn:
            self.conn.close()
            #关闭连接对象后，对象还存在内存中，需要手动设置为none
            self.conn = None

    #一、主要执行方法    在外界调用此方法即可完成数据库响应操作
        #执行主方法前需保证有游标对象，由于数据库可能存在断联等情况，故用try cash
    def get_sql_one(self,sql):
        #1.定义游标对象及数据变量
        sursor = None
        data = None
        try:
            #2.获取游标对象
            sursor = self.get_cursor()
            #3.调用执行方法
            sursor.execute(sql)
            #4.获取结果
            data = sursor.fetchone()
        except Exception as e:
            print("get_sql_one error:" , e)
        finally:
            #5.关闭游标对象
            self.close_cursor(sursor)
            #6.关闭连接对象
            self.close_conn()

            #7.返回执行结果
            return data

    #二、获取所有数据库结果集(将fetchone改为fetchall方法即可)
    def get_sql_all(self,sql):
        # 1.定义游标对象及数据变量
        sursor = None
        data = None
        try:
            # 2.获取游标对象
            sursor = self.get_cursor()
            # 3.调用执行方法
            sursor.execute(sql)
            # 4.获取所有结果集
            data = sursor.fetchall()
        except Exception as e:
            print("get_sql_one error:", e)
        finally:
            # 5.关闭游标对象
            self.close_cursor(sursor)
            # 6.关闭连接对象
            self.close_conn()

            # 7.返回执行结果
            return data

    #三、修改删除新增数据操作（删除获取对象和返回结果，增加事务提交和回滚）
    def update_sql(self,sql):
        # 1.定义游标对象及数据变量
        sursor = None
        data = None
        try:
            # 2.获取游标对象
            sursor = self.get_cursor()
            # 3.调用执行方法
            sursor.execute(sql)
            #4.事务提交
            self.conn.commit()
        except Exception as e:
            #5.事务回滚
            self.conn.rollback()
            print("get_sql_one error:", e)
        finally:
            # 5.关闭游标对象
            self.close_cursor(sursor)
            # 6.关闭连接对象
            self.close_conn()


