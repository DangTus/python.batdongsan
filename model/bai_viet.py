import datetime


class bai_viet_class:
    __format_day = "%Y-%m-%d"
    __don_vi_dien_tich = 'm²'

    # constructor'
    def __init__(self):
        pass

    # set
    def set_ten(self, ten):
        self.__ten = ten

    def set_gia(self, gia):
        if('Giá thỏa thuận' in gia):
            self.__gia = -1
        else:
            so_tien = float(gia.split(' ')[0])
            don_vi = gia.split(' ')[1]
            if('tỷ' in don_vi):
                self.__gia = so_tien * 1000000000
            elif('triệu' in don_vi):
                self.__gia = so_tien * 1000000

    def set_dia_chi(self, dia_chi):
        self.__quan = dia_chi.split(',')[0]
        self.__tinh = dia_chi.split(',')[1]

    def set_ngay(self, date):
        ngay = int(date.split('/')[0])
        thang = int(date.split('/')[1])
        nam = int(date.split('/')[2])
        x = datetime.datetime(nam, thang, ngay)
        self.__ngay = x.strftime(self.__format_day)

    def set_listlinkanh(self, list_link_anh):
        self.__list_link_anh = list_link_anh

    def set_dientich(self, dien_tich):
        self.__dien_tich = dien_tich.replace(self.__don_vi_dien_tich, '').strip()

    # get

    def get_ten(self):
        return self.__ten

    def get_gia(self):
        return round(self.__gia)

    def get_quan(self):
        return self.__quan

    def get_tinh(self):
        return self.__tinh

    def get_ngay(self):
        return self.__ngay

    def get_listlinkanh(self):
        return self.__list_link_anh

    def get_dientich(self):
        return self.__dien_tich
