import mysql.connector
from model import bai_viet

class connect():

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bat_dong_san"
        )

        self.mycursor = self.mydb.cursor()

    def close(self):
        self.mydb.close()


def get():
    conn = connect()
    mycursor = conn.mycursor
    list=[]
    bv = bai_viet.bai_viet_class()
    mycursor.execute("SELECT * FROM bai_viet")
    
    bv.set_ten('ads')
    list.append(bv)
    
    bv.set_ten('adsaa')
    list.append(bv.__dict__)
    return list
    myresult = mycursor

    for x in myresult:
        print(x)
        

    conn.close()



