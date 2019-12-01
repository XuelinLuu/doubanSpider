def write_csv(n):
    import csv
    from produce_wordcloud import getOnePageComment
    csvFile=open(r"E:\PycharmProjects\doubanSpider-master\books\book%s.csv"%n,encoding="utf-8")
    reader=csv.reader(csvFile) #以csv文件格式打开
    result={}
    for item in reader:
        if reader.line_num==1:
            continue
        result[item[0]]=item[1][32:40]
    for value in result.values():
        if value.endswith("/"):
            value=value[:-1]
    csvFile.close()
#write_csv(0)

    for each_key in result.keys():
        getOnePageComment(each_key,n,result[each_key])

if __name__=="__main__":
    write_csv("1")
