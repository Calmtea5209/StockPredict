import twstock
stock = twstock.Stock("2330")

print("近31個收盤價:")
print(stock.price)
print("近5個收盤價:")
print(stock.price[-6:])

real = twstock.realtime.get('2330') #及時交易資訊
if real["success"]:
    print("股票名稱、即時股票資料:")
    print("股票名稱:",real["info"]["name"])
    print("開盤價:",real["realtime"]["open"])
    print("最高價:",real["realtime"]["high"])
    print("最低價:",real["realtime"]["low"])
    print("目前股價:",real["realtime"]["latest_trade_price"])
else:
    print("錯誤:",real["rtmessage"])