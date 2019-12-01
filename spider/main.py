import spider.spidersGo as ssg
import pandas as pd
import numpy as np
if __name__ == '__main__':
    #res = ssg.book_spider(['科技',"教育","人文","育儿","情感"])
    res = ssg.book_spider(['科技',"教育"])
    for k in range(len(res)):
        ress = np.array(res[k]).T
        save_books = {"title": ress[0],
                      "book_url":ress[1],
                      "book_rate":ress[2],
                      "author_info":ress[3],
                      "pub_info":ress[4],
                      "out_year":ress[5],
                      "book_price":ress[6],
                      "book_cover":ress[7],
                      "people_num":ress[8]
                      }
        print(len(res[0]))
        data_frame = pd.DataFrame(save_books)
        data_frame.to_csv("..\\books\\book"+ str(k) + ".csv", index=False,sep=",", encoding="utf-8")
        print("finish")

