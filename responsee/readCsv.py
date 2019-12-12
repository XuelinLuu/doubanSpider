import pandas as pd

def readCsv(csv_name):
    path = "../books/" + csv_name
    print(path)
    csv_data = pd.read_csv(path)
    #csv_batch_data = csv_data.tail(N)  # 取后5条数据
    #print(csv_batch_data.shape)  # (5, 9)
    #train_batch_data = csv_batch_data[list(range(3, 6))]  # 取这20条数据的3到5列值(索引从0开始)
    #print(train_batch_data)

    #print(csv_data.values)
    #print(type(csv_data))
    return csv_data.values

if __name__ == '__main__':
    res = readCsv("book0.csv")
    print(res)