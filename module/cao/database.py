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
            ORDER BY ngay DESC \
            LIMIT 10'

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    list_top10_id_moinhat = []

    for x in myresult:
        list_top10_id_moinhat.append(x[0])

    conn.close()

    return list_top10_id_moinhat


def them_tinh(ten_tinh):
    #conn = connect()
    #mycursor = conn.mycursor
    #mydb = conn.mydb

    sql = f'INSERT IGNORE INTO tinh_thanh(ten_tinh) VALUES("{ten_tinh}")'
    return sql
    # mycursor.execute(sql)
    # mydb.commit()
    # mydb.close()


def them_quan(ten_quan, ten_tinh):
    #conn = connect()
    #mycursor = conn.mycursor
    #mydb = conn.mydb

    sql = f'INSERT IGNORE INTO quan_huyen (id_tinh,ten_quan) VALUES (get_id_tinh("{ten_tinh}"), "{ten_quan}")'
    return sql
    # print(sql)
    # mycursor.execute(sql)
    # mydb.commit()
    # mydb.close()


def them_bai_viet_vao_database(list_bv):
    conn = connect()
    mycursor = conn.mycursor
    mydb = conn.mydb
    sql_tinh = 'INSERT IGNORE INTO tinh_thanh(ten_tinh) VALUES '
    sql_huyen = 'INSERT IGNORE INTO quan_huyen (id_tinh,ten_quan) VALUES '
    sql_bai_viet = f'INSERT INTO bai_viet (id_baiviet, ten, id_quan, ngay, dien_tich, tong_gia) VALUES '
    sql_link_anh = f'INSERT INTO anh (id_baiviet, link) VALUES '

    for item in list_bv:
        # them sql tinh
        sql_tinh += f'("{item["tinh_thanh"]}"),'

        # them sql huyen
        sql_huyen += f'(get_id_tinh("{item["tinh_thanh"]}"), "{item["quan_huyen"]}"),'

        # them bai viet
        sql_bai_viet += f'("{item["id"]}","{item["ten"]}",get_id_quan("{item["quan_huyen"]}"), \
                        "{item["ngay_dang"]}","{item["dien_tich"]}","{item["gia"]}"),'
        # print(item['id'])
        for item_anh in item['list_link_anh']:
            sql_link_anh += f'("{item["id"]}","{item_anh}"),'

    sql_tinh = sql_tinh.rstrip(",")
    sql_huyen = sql_huyen.rstrip(",")
    sql_bai_viet = sql_bai_viet.rstrip(",")
    sql_link_anh = sql_link_anh.rstrip(",")

    mycursor.execute(sql_tinh)
    mycursor.execute(sql_huyen)
    mycursor.execute(sql_bai_viet)
    mycursor.execute(sql_link_anh)

    mydb.commit()

    conn.close()
