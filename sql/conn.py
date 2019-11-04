import pymysql
import json

def connnect_db():
    loop_num = 0
    with open("connj.json", "r") as fp:
        connj = json.load(fp)

    #print(connj)

    while True:
        loop_num += 1
        try:
            conn = pymysql.connect(**connj)
            print("connect successfully")
            return conn
        except Exception as e:
            print(e.args)
            if loop_num > 10:
                print("fail to connect the database.")
                return False
            else:
                continue

if __name__ == '__main__':
    a = connnect_db()
    print(a)


