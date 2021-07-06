import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
headers={"User-Agent":str(UserAgent().random)}
import jieba
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
import os

def getOnePageComment(name,n,id):
    #得到三页短评
    global pagenum
    pagenum=0
    comments = ""
    for pagenum in range(3):
        url="https://book.douban.com/subject/%s/comments/hot?p=%d"%(id,pagenum)
        content=requests.get(url,headers=headers).text
        soup=BeautifulSoup(content,"html5lib")
        commentsList=soup.find_all("span",class_="short")
        for commentTag in commentsList:
            comments+=commentTag.string
        pagenum+=1
    if not os.path.exists("book%s_pic"%n):
        os.mkdir("book%s_pic"%n)
    with open("book%s_pic\%s.txt" %(n,name),"w",encoding="utf-8") as f:
            f.write(comments)

    #生成词云
    del_words=["小说","没有","觉得","不过","作者","时候","故事","一个","非常","那么","这样","不是","可以","还是","本书","就是","什么","自己","如果","看到","还有","对于","最后","这个","因为","已经","方面"]
    with open("book%s_pic\%s.txt"%(n,name), encoding="utf-8")as f:
        txt = f.read()
    mask = np.array(Image.open("0060530067.jpg"))
    mytxt=list(jieba.cut(txt))
    for each in mytxt:
        if each in del_words:
            mytxt.remove(each)
    final_txt=" ".join(mytxt)
    wordcloud = WordCloud(font_path="simsun.ttf", background_color="white",
                          mask=mask).generate(final_txt)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig("book%s_pic\%s.jpg"%(n,name))
    plt.show()
    os.remove("book%s_pic\%s.txt"%(n,name))

def main():
    getOnePageComment("无声告白","1","26382433")

if __name__=="__main__":
    main()









