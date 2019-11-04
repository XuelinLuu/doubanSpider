#-*- coding:utf-8 -*-
import time
import urllib.request
from bs4 import BeautifulSoup
import json
import numpy as np

import spider.numberOfPeople as nop


with open("hds.json", "r") as fp:
    hds = json.load(fp)
    #hds.json中存储的是http请求子段中的header属性值

def book_spider(book_tag):
    book_num = 0
        ##### 用来控制一共要读取多少本书
    page_num = 0
    book_list = []
    try_time = 0
    while True:
        url = 'http://www.douban.com/tag/' + urllib.request.quote(book_tag) + "/book?start=" + str(page_num * 15)
        print(url)
        #time.sleep(np.random.rand() * 5)

        try:
            req = urllib.request.Request(url, headers=hds[page_num % len(hds)])
            # 使用固定的请求头和url访问一个网址，封装成一个request类型
            source = urllib.request.urlopen(req)
            # 调用这个request类型，将返回的值存储到source中
            source_code = source.read().decode("utf-8")
            # 对source中的数据进行解码
            plain_text = str(source_code)
            print(type(plain_text))



        except Exception as e:
            print(e.args)
            continue

        soup = BeautifulSoup(source_code, 'lxml')
        #print(soup)
        list_soup = soup.find('div', {'class': 'mod book-list'})
        #在格式化的数据中查找class为mod book-list的词条
        try_time += 1
        #如果请求访问网址的时间超过200就不不去找了，拜拜
        if list_soup == None and try_time < 200:
            print("try times = {0} < 200 so try again".format(try_time))
        elif list_soup == None or len(list_soup) <= 1:
            break

        #通过soup进行各种查询，各种分类，理解需要对html代码进行理解，可以在chrome中使用f12查看。
        for book_info in list_soup.findAll('dl'):
            title = book_info.find('a', {"class" : "title"}).string.strip()
            desc = book_info.find('div', {"class" : "desc"}).string.strip()
            desc_list = desc.split("/")
            book_url = book_info.find("a", {"class" :"title"}).get("href")
            try:
                book_rate = book_info.find("span", {"class" : "rating_nums"}).string.strip()
            except:
                book_rate = ""
            try:
                book_cover = book_info.find("img").get("src")
            except:
                book_cover = ""
            try:
                author_info = desc_list[0 : -3]
            except:
                author_info = ""
            try:
                pub_info = desc_list[-3]
            except:
                pub_info = ""
            try:
                out_year = desc_list[-2]
            except:
                out_year = ""

            try:
                book_price = desc_list[-1]
            except:
                book_price = "0"
            try:
                people_num = nop.get_number_of_people(book_url)
            except:
                people_num = ""



            book_list.append([title, book_url, book_rate, author_info, pub_info, out_year, book_price, book_cover, people_num])
            book_num += 1

            try_time = 0

            ### 此处可以注释掉
            print("书    名： ", title)
            print("网    址： ", book_url)
            print("排    名： ", book_rate)
            print("作    者： ", author_info)
            print("出版  社： ", pub_info)
            print("出版年月： ", out_year)
            print("价    格： ", book_price)
            print("封面网址： ", book_cover)
            print("评价人数： ", people_num)

            if book_num >= 100:
                break


        page_num += 1
        if book_num >= 100:
            break
    return book_list
if __name__ == '__main__':
    book_spider("科技")