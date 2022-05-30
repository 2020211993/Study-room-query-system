import sqlite3
def create(date):
    conn = sqlite3.connect("classMessage.db")#在此文件所在的文件夹打开或创建数据库文件
    c = conn.cursor()#设置游标
    tableName = '星期' + str(date)#设置表的名字
    #创建表
    c.execute('''CREATE TABLE '星期1'
            (classroom text, 
            building text,
            floor int,
            '1' text,
            '2' text,
            '3' text,
            '4' text,
            '5' text,
            '6' text,
            '7' text,
            '8' text,
            '9' text,
            '10' text,
            '11' text,
            '12' text,
            '13' text,
            '14' text,
            occupied text,
            people int)''')
    conn.commit()#保存
    print("新建数据表完成")
    conn.close()#关闭连接

if __name__ == '__main__':
    create(1)