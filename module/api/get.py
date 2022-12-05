import mysql.connector


class connect():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bat_dong_san"
        )
        self.mycursor = self.mydb.cursor(dictionary=True)

    def close(self):
        self.mydb.close()


def get_anh(id_baiviet):
    conn = connect()
    mycursor = conn.mycursor

    sql = f'SELECT link \
            FROM anh \
            WHERE id_baiviet = {id_baiviet}'

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    list_hinh_anh = []

    for x in myresult:
        list_hinh_anh.append(x['link'])

    conn.close()

    return list_hinh_anh


def get_bai_viet(gia_min, gia_max, quan_huyen, tinh_thanh):
    conn = connect()
    mycursor = conn.mycursor

    sql = f'SELECT id_baiviet, ten, ngay, ten_quan, ten_tinh, dien_tich, tong_gia \
            FROM bai_viet, quan_huyen, tinh_thanh \
            WHERE bai_viet.id_quan = quan_huyen.id_quan \
	            and quan_huyen.id_tinh = tinh_thanh.id_tinh '

    if (gia_min):
        sql += f'and tong_gia < {gia_min} '
    if (gia_max):
        sql += f'and tong_gia < {gia_max} '
    if (quan_huyen):
        sql += f'and ten_quan = "{quan_huyen}" '
    if (tinh_thanh):
        sql += f'and ten_tinh = "{tinh_thanh}" '

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        x['tong_gia'] = 'Giá thỏa thuận' if x['tong_gia'] == -1 else x['tong_gia']
        x.__setitem__('link_hinh_anh', get_anh(x['id_baiviet']))

    conn.close()

    return myresult
