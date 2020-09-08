#スタティックメソッド
class Car():
    kind = "toyota"
    def __init__(self):
        self.x = 10

    @staticmethod
    def year():
        print(2000)

print(Car.year())

# スタティックメソッドは、オブジェクトを生成していなくても呼び出せる関数
# 外部に関数を書いているのと同じ
# ただし、クラス内に記述したほうが分かり易いときは使うとよい
