class Hello(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name_age(self):
        print("%:%" % (self.name, self.age))


from types import MethodType


def set_age(self, age):
    self.age = age


class Person(object):

    def __str__(self):
        return "Test"

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def name(self, name):
        if not isinstance(name, (str)):
            raise ValueError("输入内容错误")
        else:
            self._name = name

    @age.setter
    def age(self, age):
        if not isinstance(age, (int, float)):
            raise ValueError("请输入int或float类型的参数")
        elif age == 0:
            raise ValueError("不能输入0")
        elif age > 100:
            raise ValueError("请输入正确的年龄")
        else:
            self._age = age

    def test(self, Hello):
        test_age = Hello.age
        test_name = Hello.name
        return test_name,test_age




def foo(i):
    assert i != 0, 'i is zero'
    n = 10 / i
    return n


if __name__ == '__main__':
    h = Hello("zhang", 19)
    p=Person("li",10)
    pname,page=p.test(h)
    print("name",pname,"age",page)

    # h2 = Hello('li', 20)
    # h.set_age = MethodType(set_age, h)
    # Hello.set_age = set_age
    # h.set_age(10)
# h2.set_age(20)
# print(h2.age)
# print(h.age)
# per = Person('zhang', 20)
# per.age = 1
#
# print(per.age)
# # print(per.name)
# print(per)
# try:
#     a = foo(0)
#     print(a)
# except ZeroDivisionError as e:
#     print(e)
# finally:
#     print("finally")

# a = 3
# if a == 3:
#     mag = 'hello'
#
# print(mag)
