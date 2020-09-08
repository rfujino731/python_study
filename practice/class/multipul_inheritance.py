#クラスの多重継承
#多重継承：複数のクラスを１つのクラスが継承すること
#不必要に使わないこと
class Person(object):
    def talk(self):
        print("talk")

    def run(self):
        print("person run")

class Car(object):
    def run(self):
        print("car run")

#以下多重継承の記述(引数に複数のクラス名を書くだけ)
#左側に書いたクラスが優先される(同じメソッドがあったときは、左側に記述してあるクラスが優先される)
class PersonCarRobot(Person, Car):
    def fly(self):
        print("fly")

person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.fly()
