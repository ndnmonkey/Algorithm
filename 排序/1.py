#super() 函数是用于调用父类(超类)的一个方法。
#super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。
#MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。
class A:
    def add(self, x):
        y = x + 1
        print(y)

class B(A):
    def add(self, x):
        super().add(x)

b = B()
b.add(2)  # 3