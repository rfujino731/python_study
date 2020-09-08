
#class変数
class Person(object):
    #kind変数がクラス変数
    #クラス内ならself.kindで呼び出せる
    kind = "hunman"
    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)

a = Person("A")
print(a.who_are_you())
b = Person("B")
print(b.who_are_you())
