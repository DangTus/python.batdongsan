from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import datetime
from model import bai_viet

ser = Service("./lib/chromedriver.exe")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=ser, options=op)


def xu_ly_gia(gia):
    if ('Giá thỏa thuận' in gia):
        return -1
    else:
        so_tien = float(gia.split(' ')[0])
        don_vi = gia.split(' ')[1]
        if ('tỷ' in don_vi):
            return so_tien * 1000000000
        elif ('triệu' in don_vi):
            return so_tien * 1000000


def lay_anh(bai_viet_html):
    list_hinh_anh = bai_viet_html.find_elements(
        'xpath', './/img')

    list_hinh_anh_bai_viet = []

    for hinh_anh in list_hinh_anh:
        if (hinh_anh.get_attribute('data-listing')):
            anh = hinh_anh.get_attribute('data-listing').split(',')
            list_hinh_anh_bai_viet.extend(anh)
        else:
            anh = hinh_anh.get_attribute('data-src')
            list_hinh_anh_bai_viet.append(anh)

    return list_hinh_anh_bai_viet


def xu_ly_ngay(date):
    format_day = "%Y-%m-%d"

    ngay = int(date.split('/')[0])
    thang = int(date.split('/')[1])
    nam = int(date.split('/')[2])
    x = datetime.datetime(nam, thang, ngay)

    return x.strftime(format_day)

def xu_ly_dientich(dien_tich):
    don_vi_dien_tich = 'm²'
    return dien_tich.replace(don_vi_dien_tich, '').strip()


def cao_bai_viet():
    global bai_viet

    browser.get("https://batdongsan.com.vn/nha-dat-ban")

    list_bai_viet_html = browser.find_elements(
        'xpath', '//div[@id="product-lists-web"]/div')

    list_bai_viet = []

    for bai_viet_html in list_bai_viet_html:
        bv = bai_viet.bai_viet_class()

        tieu_de = bai_viet_html.find_element(
            'xpath', './/h3[@class="re__card-title"]/span').text
        bv.set_ten(tieu_de)

        gia = bai_viet_html.find_element(
            'xpath', './/span[@class="re__card-config-price"]').text
        bv.set_gia(xu_ly_gia(gia))

        dia_chi = bai_viet_html.find_element(
            'xpath', './/div[@class="re__card-location"]').text
        quan = dia_chi.split(',')[0]
        tinh = dia_chi.split(',')[1]
        bv.set_tinhthanh(tinh)
        bv.set_quanhuyen(quan)

        ngay = bai_viet_html.find_element(
            'xpath', './/div[@class="re__card-published-info"]/span[@aria-label]').get_attribute('aria-label')
        bv.set_ngay(xu_ly_ngay(ngay))

        dien_tich = bai_viet_html.find_element(
            'xpath', './/span[@class="re__card-config-area"]').text
        bv.set_dientich(xu_ly_dientich(dien_tich))

        list_link_anh = lay_anh(bai_viet_html)
        bv.set_listlinkanh(list_link_anh)

        # in
        print(bv.__dict__, '\n\n')
