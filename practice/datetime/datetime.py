import datetime

#現在の時間を取得
now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime("%d/%m/%y-%H"))

#現在の日付を取得
today = datetime.date.today()
print(today)
print(today.isoformat())
print(today.strftime("%d/%m/%y-%H"))

#時間データを自作する
t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t)
print(t.isoformat())
print(t.strftime("%d/%m/%y-%H"))

#一年前の日付を所得
d1 = datetime.timedelta(days=365)
print(now - d1)

#10日前の日付を取得
d2 = datetime.timedelta()

#タイムスリープ
import time
#下記コードだと5秒間コードの実行が止まる
print("start")
time.sleep(5)
print("finish")
