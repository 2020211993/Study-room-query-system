import sqlite3
import pandas as pd
import re

def insert(date):
    con = sqlite3.connect('classMessage.db')
    c = con.cursor()#设置游标
    df = pd.read_excel(date+'.xlsx')#打开xlsx对象
    for i in range(len(df)):
        data = df.iloc[i].values#读取行信息
        classroom = df.iloc[i,0]#读取classroom信息
        #正则表达式识别classroom字段
        classroomRegex = re.compile(r'([N,S]\d)-(\d)|([N,S])(\d)')
        mo = classroomRegex.search(classroom)
        try:
            if len(mo.group(0)) == 2:
                building = mo.group(0)[0]
                floor = mo.group(0)[1]
            else:
                building = mo.group(1)
                floor = mo.group(2)
            #print(building, floor)
            #写入数据表
            sql = '''insert into 星期1 (classroom, building, floor, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', occupied, people)
            values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);'''
            dataList = [(data[0], building, floor, data[1], data[2], data[3], data[4], data[5],data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], 0, 0)]
            c.executemany(sql, dataList)
            #c.execute('update '+date+' set name="people" where id=2', str(0))
        except:
            continue
    con.commit()
    con.close()
    print("数据存入完成")

if __name__ == '__main__':
    insert('星期1')