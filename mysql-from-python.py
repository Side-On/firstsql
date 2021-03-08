import os
import pymysql

#Get username from Cloud9 workspace
# (modify this variable if running on another environment)

username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
user=username,
password = '',
db='Chinook')

try:
    #run a query
    with connection.cursor() as cursor:
        sql = 'SELECT * FROM Artist;'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    #close connection, regardless if it works or not
    connection.close()