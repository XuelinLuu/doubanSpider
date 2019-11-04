import spider.aSpider as spd

def start_a_spider(book_tag_list):
    book_lists = []
    for book_tag in book_tag_list:
        book_list = spd.book_spider(book_tag)   #将种类中的各种种类分别进行查找，返回的值是一个list
        book_lists.append(book_list)    #将返回的list添加到一个更大的list中，后续可以进行入库处理
    return book_lists
if __name__ == '__main__':
    a = start_a_spider(["科技"])  #列表中的是要查找的所有图书的种类
    print(a)