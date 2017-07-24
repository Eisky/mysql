import pymysql


class MySqlHelper(object):
    def __init__(self):
        pass

    def get_dict(self, sql, params):
        conn = MySQLdb.connect(host='127.0.0')
        cur = conn.cursor(cursorClass=pymysql.cursors.DictCursor)
        recount = cur.execute(sql, params)
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data

    def get_one(self, sql, params):
        conn = pymysql.connect(host='127.0.0')
        cur = conn.cursor(cursorClass=MySQLdb.cursors.DictCursor)
        recount = cur.execute(sql, params)
        data = cur.fetchone()
        cur.close()
        conn.close()
        return data


a = MySqlHelper()
sql = 'select * from admin where id>%s'
params = (1,)

simple_data = a.get_one(sql, params)
complex_data = a.get_dict(sql, params)
