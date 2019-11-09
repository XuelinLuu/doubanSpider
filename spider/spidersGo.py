#-*- coding:utf-8 -*-
'''
这是对爬取到的数据进行处理
拆分到具体的数据类型
'''

import time
import urllib.request
from bs4 import BeautifulSoup
import json
import numpy as np


import spider.numberOfPeople as nop
import spider.spiderAio as saio

def book_spider(book_tags):
    iiiii = 0
    len_book_tags = len(book_tags)
    # 书的种类的长度
    book_list = [[] for i in range(len_book_tags)]


    # 一个循环搜索一个种类，但是这个种类同时爬取几个页面
    for i in range(len_book_tags):
        book_num, page_num, want_page = 0, -1, 1
        # 修改 want_page 的值可以查询更多页面
        urls = []
        book_tag = book_tags[i]

        for book_num in range(want_page):
            page_num += 1
            url = 'http://www.douban.com/tag/' + urllib.request.quote(book_tag) + "/book?start=" + str(page_num * 15)
            # 暂时先查看第一个页面
            # url = 'http://www.douban.com/tag/' + urllib.request.quote(book_tags[i]) + "/book?start=" + str(page_num * 15)
            urls.append(url)

        source = saio.getAllWebPage(urls)
        # return  string  "" or a page(string)
        # 返回的是一个list，是所有url对应的页面

        for j in range(want_page):


            source_code = source[j]
            # 这是每一个url返回的界面
            if source_code == "":
                continue

            soup = BeautifulSoup(source_code, 'lxml')
            # print(soup)
            list_soup = soup.find('div', {'class': 'mod book-list'})
            # 在格式化的数据中查找class为mod book-list的词条

            #通过soup进行各种查询，各种分类，理解需要对html代码进行理解，可以在chrome中使用f12查看。
            for book_info in list_soup.findAll('dl'):

                # page_num还是有待使用，用来查询第二个数据的页面

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



                book_list[i].append([title, book_url, book_rate, author_info, pub_info, out_year, book_price, book_cover, people_num])
                book_num += 1

                try_time = 0

                ### 此处可以注释掉
                iiiii += 1
                print(iiiii)
                print("书    名： ", title)
                print("网    址： ", book_url)
                print("排    名： ", book_rate)
                print("作    者： ", author_info)
                print("出版  社： ", pub_info)
                print("出版年月： ", out_year)
                print("价    格： ", book_price)
                print("封面网址： ", book_cover)
                print("评价人数： ", people_num)


    return book_list
if __name__ == '__main__':
    book_spider(["科技", "音乐"])
