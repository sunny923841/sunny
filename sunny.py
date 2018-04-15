#声明一个Employee类
class Employee:
#声明一个类的变量
    pay_raist_amount=1.2
    __weight=40   
#创建一个构造器
    def __init__(self,first,last,pay,weight,domain="funcat.com"):
        self.first=first
        self.last=last
        self.pay=pay
# self.email=first+last+"@email.com"
        self.email=first+last+"@"+domain
        self.__weight=50

#创建一个方法
    def fullname(self):
        return '{}-{}-{}'.format(self.first,self.last,self.pay)
    
    def new_pay(self):
        return self.pay * self.pay_raist_amount
    def new_pay1(self):
        return self.pay * Employee.pay_raist_amount
    def _say(self):
        print("hello world {}".format(self.__weight))
    def Isay(self):
        self._say()

#创建一个类的实例
emp1=Employee("sunny","Li",1000,50,"baidu.com")
emp2=Employee("Lucy","Wang",2000,"sina.com")
emp1.Isay()
# print(emp1.first,emp1.last,emp1.pay,emp1.email)
# print(emp2.first,emp2.last,emp2.pay,emp2.email)
# print(emp1.fullname())
# print(emp1.new_pay())
# Employee.pay_raist_amount=1.4
# print("用类名调用pay")
# print(emp1.new_pay())
# print(emp1.new_pay1())
# print(emp2.new_pay())
# print(emp2.new_pay1())
# emp1.pay_raist_amount=1.5
# print("用emp1设置pay的值")
# print(emp1.new_pay())
# print(emp1.new_pay1())
# print(emp2.new_pay())
# print(emp2.new_pay1())
# emp2.pay_raist_amount=1.6
# print("用emp2设置pay的值")
# print(emp1.new_pay())
# print(emp1.new_pay1())
# print(emp2.new_pay())
# print(emp2.new_pay1())
# print(emp1.fullname())


