import csv
import matplotlib.pyplot as plt
import pandas as pd
import twstock
import time
import os
	
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] #設定中文字體
 
filepath =  "year2022.csv"

if not os.path.isfile(filepath):
    title = ["日期","成交股數","成交金額","開盤價","收盤價","最高價","最低價","漲跌價差","成交量"]

    outputfile = open(filepath,"a",newline="",encoding="big5")
    outputwriter = csv.writer(outputfile)
    for i in range(1,7):
        stock = twstock.Stock("2330")
        stocklist = stock.fetch(2022,i)
        data = []
        for stock in stocklist:
            strdate = stock.date.strftime("%Y-%m-%d") #格式化時間
            l = [strdate,stock.capacity,stock.turnover,stock.open,stock.close,stock.high,stock.low,stock.change,stock.transaction]
            data.append(l)
        if i==1:
            outputwriter.writerow(title)
        for dataline in data:
            outputwriter.writerow(dataline)
        time.sleep(6)
            
    outputfile.close()

pdstock = pd.read_csv(filepath,encoding="big5")
pdstock["日期"] = pd.to_datetime(pdstock["日期"])
pdstock.plot(kind='line',figsize=(12,6),x='日期',y=['收盤價','最低價','最高價'])
plt.show()