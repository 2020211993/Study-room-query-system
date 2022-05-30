import pandas as pd

def xlsx_to_csv():
    data_xls = pd.read_excel('星期1.xlsx', index_col=0)
    data_xls.to_csv('星期1.csv', encoding='utf-8')

if __name__ == '__main__':
    xlsx_to_csv()