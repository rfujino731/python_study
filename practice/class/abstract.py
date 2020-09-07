#抽象クラスについて
#サブクラスで共通で必要な処理を記事する
#サブクラスで記述を忘れると、エラーになる
#下記コードでは(23,24もしくは33,34行目をコメントアウトするとエラーになる)
#※下記コードは正常であれば、何も表示されずに終了する。
#スーパークラスでは、インスタンスは生成されない


import abc

class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    @abc.abstractmethod
    def drive(self):
        pass
    #Personクラスのdriveは継承したクラスでは必ず実装しなさいという意味
    #Personの中では実行されない

class Baby(Person):
    def __init__(self, age = 1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        raise Exception("No drive")

class Adult(Person):
    def __init__(self, age = 18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        raise Exception("No drive")

baby = Baby()
adult = Adult()
