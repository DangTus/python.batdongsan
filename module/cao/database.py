import mysql.connector


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


def get_top10_id_moinhat():
    conn = connect()
    mycursor = conn.mycursor

    sql = f'SELECT id_baiviet \
            FROM bai_viet \
            LIMIT 10'

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    list_top10_id_moinhat = []

    for x in myresult:
        list_top10_id_moinhat.append(x[0])

    conn.close()

    return list_top10_id_moinhat


def them_bai_viet_vao_database():
    conn = connect()
    mycursor = conn.mycursor

    sql = f'SELECT id_baiviet \
            FROM bai_viet \
            LIMIT 10'

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    list_top10_id_moinhat = []

    for x in myresult:
        list_top10_id_moinhat.append(x[0])

    conn.close()

    return list_top10_id_moinhat
