import os
import MySQLdb
db = MySQLdb.connect(host="localhost", user="root", passwd="bl3000", db="shop", charset='cp1251')
cursor = db.cursor()
folder = "productions"
images = os.listdir("../static/img/%s" % (folder))
for x in images:
    x.decode('cp1251')
    insert = (""" "%s" , 0, "","%s" """ % (x[:-4], 'img/%s/%s' % (folder,x)))
    cursor.execute("Insert Into shop_bads Values (null,%s)" % (insert))
db.commit()