def outer(a):
    def inner(b):
        print(b * 5)
        return
    return inner(a)#関数を戻り値に設定している
outer(5)
