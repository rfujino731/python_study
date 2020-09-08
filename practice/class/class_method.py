#クラスメソッド
class Car():
    kind = "toyota"
    def __init__(self):
        self.x = 10

    @classmethod
    #クラスとしてオブジェクトが生成されていなくても関数を呼び出したいときに使う
    def what_is_kind(cls):
        return cls.kind

a = Car()
print(a.what_is_kind())
b = Car#「()」がないとオブジェクトが生成されない
print(b.what_is_kind())#エラーになる


class Car():
    kind = "toyota"
    def __init__(self):
        self.x = 10

    def what_is_kind(self):
        return self.kind

a = Car()
print(a.what_is_kind())
#b = Car#「()」がないとインスタンスが生成されない
#print(b.what_is_kind())#エラーになる
