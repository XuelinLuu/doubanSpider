import socketio
import eventlet
import random
import pymysql

# 实例化socketio对象
sio = socketio.Server()


@sio.on('connect')
def connect(sid, environ):
    print('environ123', environ)


#  监听前端传入的请求数据
# 根据请求数据连接数据库获取目标数据
@sio.on('message')
def message(sid, data):
    print('message', data)
    if data == 'getContentList':
        # 连接数据库
        db = pymysql.connect('localhost', 'root', '123456', 'python1')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # mysql语句
        sql = 'select item_id,item_title,item_image,item_price,num from tb_cart;'
        # 执行sql语句
        cursor.execute(sql)
        # 获取所有游标
        data1 = cursor.fetchall()
        # 因为data1为元组，到传到前端只能读取到一条信息，所以要转成列表
        data = list(data1)
        # 给前端返回数据标名数据类型，前端好区分需求数据
        content = {'type': 'getContentList', 'data': data}
        print(data, '12311111')
        # 将整理好的数据返回到前端
        sio.emit('reply', content)


@sio.on('disconnect')
def disconnect(sid):
    print('disconnect123', sid)


if __name__ == '__main__':
    # sio通过middleware转为应用服务
    app = socketio.Middleware(sio)

    # 依赖eventlet网关服务器
    eventlet.wsgi.server(eventlet.listen(('', 7444)), app)