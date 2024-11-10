import pymysql

def get_db():
    connection = pymysql.connect(
        host='localhost', 
        user='root', 
        database='anjungan', 
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection