'''
有的类的方法中第一参数是cls，有的是self，经过了解得知，python并没有对类中
方法的第一个参数名字做限制，可以是self，也可以是cls，不过根据人们的惯用用
法，self一般是在实例方法中使用，而cls则一般在类方法中使用，在静态方法中则
不需要使用一个默认参数，其实这个默认参数可以换成任何一个名字代替，不会产生
任何影响。
'''
class Person(object):
    class_integer = 10
    def __init__(self, name):
        self.name = name

    #普通方法
    def talk(self):
        print("talk方法：",self.name)
    #静态方法,静态方法不能访问实例变量
    @staticmethod
    def speak():
        print('%s is speaking chinese.' )

    @staticmethod
    def speak1():
        print('Anyone is speaking chinese.' )
    #类方法,类方法和普通方法的区别是， 类方法只能访问类变量，不能访问实例变量
    @classmethod
    def nationality(self):
        print('Bigberg is %s.' % self.name)

    @classmethod
    def nationality1(cls):  #改为cls
        print('Bigberg is %s.' % cls.class_integer)
    #属性方法
    @property
    def drive(self):
        print('%s is driving a car.' % self.name)
    #setter方法，想在在属性方法里传参，比如车的品牌，我们就要用setter了，具体用法  @属性方法名.setter　


p = Person('Bigberg')
p.talk()
#1，静态方法
# assert p.speak(),"静态方法不能访问实例变量"
#那么如何才能使用它呢？ --> 将实例传给自己。静态变量不能范文实例变量意味着他对类来说没啥用，除了得通过类来调用外。
p.speak(p)

#如果静态方法不带self呢？
p.speak1()

#2，类方法
# p.nationality()

#如果访问类变量class_integer是可以的，但是实例代入的变量就不行。
p.nationality1()

#3，属性方法
# p.drive()  #这里会出错：'NoneType' object is not callable，因为添加@property后成一个静态属性了，不是方法了，像变量一样调用它就行了(不带括号)。
p.drive
