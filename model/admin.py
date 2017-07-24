from utility.sqlhelper import MySqlHelper


class Admin(object):
    def __init__(self):
        self.__helper = MySqlHelper()

    def get_one(self, id):
        sql = 'select * from admin where id = %s'
        params = (id,)
        return self.__helper.get_one(sql, params)
    def CheckValidate(self,username, password):
        sql = 'select * from admin where name = %s'
        params = (username, password)
        return self.__helper.get_one(sql,params)

if __name__ = '__main__':
    main()
