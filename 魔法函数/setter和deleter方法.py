class Person(object):
    country = 'Chinese'

    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.car = "LAMBORGHINI"  # 当然这里也可以设置为私有属性

    @property
    def drive(self):  # 这里不能传参是因为调用的时候，p.drive 没有()了，不能传入
        print('%s is driving a %s.' % (self.name, self.car))

    # setter方法
    @drive.setter  # 修饰方法drive,可以为属性赋值
    def drive(self, car):  # 我们要重新定义这个drive方法
        print("set car:", car)
        self.car = car

    # deleter
    @drive.deleter  # 修饰 drive 方法，可以删除属性
    def drive(self):  # 重新定义 drive方法
        del self.car  # 删除的是属性
        print("扣了你的车,让你开豪车...")


p = Person('Bigberg', 'CN')
#1，setter方法
p.drive = 'Benz'  # 给属性赋值
p.drive

#2，deleter方法
del p.drive

#使用deleter方法后就没这和属性了
p.drive