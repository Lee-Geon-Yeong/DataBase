import MySQLdb

db = MySQLdb.connect(host='localhost', db='employees',
                     user='root', passwd='wjstk0')
cursor = db.cursor()

sql = """
"""
cursor.execute(sql)

cursor.close()
db.close()