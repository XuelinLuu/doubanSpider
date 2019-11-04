import urllib.request
from bs4 import BeautifulSoup
import numpy as np
import json
def get_number_of_people(url = "https://book.douban.com/subject/33424487/?from=tag_all"):
    with open("hds.json", "r") as fp:
        hds = json.load(fp)
    #hds.json中存储的是http请求子段中的header属性值

    try:
        req = urllib.request.Request(url, headers=hds[np.random.randint(1, len(hds))%len(hds)])
            #使用固定的请求头和url访问一个网址，封装成一个request类型
        source = urllib.request.urlopen(req)
            #调用这个request类型，将返回的值存储到source中
        source_code = source.read().decode("utf-8")
            #对source中的数据进行解码

        soup = BeautifulSoup(source_code, "lxml")
            #对数据进行解析，按照html的格式
        #print(soup)
        people_num = soup.find("div", {"rating_sum"}).findAll("span")[1].string.strip()
            #通过soup对格式化之后的数据获得我们需要的数据，此处需要对html代码进行查看
        return people_num
    except Exception as e:
        print(e.args)
        return ""

if __name__ == '__main__':
    a = get_number_of_people()
    print(a)
