#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


print(abs(100))
print(abs(-100))

print(max(1, 2))
print(min(1, 2))

# 数据类型转换
# int()函数可以将其他数据类型转换为整数
print(int('1234'))
print(float('3.1415'))
print(str(1234))
print(bool(1))
print(bool(''))

# 函数名其实就是指向一个函数对象的引用，
# 完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs
print(a(-1))

# hex()可以将一个整数转换成十六进制表示的字符串

# 定义函数
# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回。


def my_abs(x):
    if x > 0:
        return x
    else:
        return -x


print(my_abs(1))
print(my_abs(-1))

# 空函数


def nop():
    pass


def testFunc(x):
    if x > 18:
        pass


# 参数检查
# 数据类型检查可以用内置函数isinstance()实现
def my_abs2(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type!')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs2(123))
print(my_abs2(123.345))
# print(my_abs2('123')) # TypeError: bad operand type!


# 函数返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y-step*math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)

# 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，
# 而多个变量可以同时接收一个tuple，按位置赋给对应的值，
# 所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

# 定义函数时，需要确定函数名和参数个数；
# 如果有必要，可以先对参数的数据类型做检查；
# 函数体内部可以用return随时返回函数结果；
# 函数执行完毕也没有return语句时，自动return None。
# 函数可以同时返回多个值，但其实就是一个tuple。


# 函数的参数
# 定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。
# 对于函数的调用者来说，只需要知道如何传递正确的参数，以及函数将返回什么样的值就够了，
# 函数内部的复杂逻辑被封装起来，调用者无需了解。

# Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，
# 还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，
# 还可以简化调用者的代码。

# 位置参数
# def power(x):  # 计算x的平方
#     return x * x

# 对于power(x)函数，参数x就是一个位置参数。
# print(power(2))

# def power(x, n):  # 计算x的n次方
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s


# print(power(2, 3))

# 修改后的power(x, n)函数有两个参数：x和n，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n。

# 默认参数


def power(x, n=2):  # 计算x的n次方
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5))

# 从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
# 二是如何设置默认参数。当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
# def enroll(name,gender):
#     print('name:', name)
#     print('gender:',gender)

# print(enroll('Sarah','female'))


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll('Sarah', 'female')
# x = enroll('Sarah', 'female')
# print(x)
# name: Sarah
# gender: female
# age: 6
# city: Beijing
# None  <=
# 前四个输出 就是执行函数的时候输出的 最后一个None值 是执行函数之后的返回值 print(返回值)
# 所以就是输出了一个None

# 有多个默认参数时，调用的时候，既可以按顺序提供默认参数，比如调用enroll('Bob', 'M', 7)，意思是，除了name，gender这两个参数外，
# 最后1个参数应用在参数age上，city参数由于没有提供，仍然使用默认值。
# 也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。比如调用enroll('Adam', 'M', city='Tianjin')，
# 意思是，city参数用传进去的值，其他默认参数继续使用默认值。

# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# def add_end(L=[]):
#     L.append('END')
#     return L

# print(add_end()) #['END']
# print(add_end()) #['END', 'END']


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())  # ['END']
print(add_end())  # ['END']


# 可变参数
# 可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# 调用函数的时候，需要将传入的参数组装成一个list或者tuple
print(calc([1, 2, 3, 4]))
print(calc((1, 3, 5, 7)))


# 利用可变参数
def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc2(1, 2, 3))
print(calc2(1, 3, 5, 7))


# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
# 但是，调用该函数时，可以传入任意个参数，包括0个参数：
print(calc2())
print(calc2(1, 2))


# 如果已经有一个list或者tuple，可以用以下方法
nums = [1, 2, 3]
print(calc2(nums[0], nums[1], nums[2]))


# 可以在list或者tuple前面加上一个*，将其变成可变参数传进去
print(calc2(*nums))
# *nums表示把nums这个list的所有元素作为可变参数传进去。


# 关键字参数
# 关键字参数允许传入0个或者任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, ', age:', age, ', other:', kw)


person('Michael', 30)


# 也可以传入任意个数的关键字参数
person('Bob', 35, cuty='Beijing')
person('Adam', 45, gender='M', job='Engineer')


# 关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，
# 但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，
# 其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。

# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。


# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数，至于到底传入了哪些，就需要在函数内部通过kw检查
def person2(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, ', age:', age, ', other:', kw)


person2('Jack', 24, city='Beijing', addr='Chaoyang', zipCode=123456)

# 如果要限制关键字参数的名字，就可以用命名关键字参数


def person3(name, age, *, city, job):
    print(name, age, city, job)


person3('Jack', 24, city='Beijing', job='Engineer')


# 如果函数定义中已经有一个可变参数，后面跟着的命名关键字参数就不在需要一个特殊分割符*了
def person4(name, age, *args, city, job):
    print(name, age, args, city, job)


# 命名关键字参数必须传入参数名，这和位置参数不同，如果没有传入参数名，调用会报错
# person('Jack', 24, 'Beijing', 'Engineer')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: person() takes 2 positional arguments but 4 were given


# 由于调用时缺少参数名city和job，Python解释器把这4个参数均视为位置参数，但person()函数仅接受2个位置参数。

# 命名关键字参数可以有缺省值，从而简化调用：
def person5(name, age, *, city='Beijing', job):
    print(name, age, city, job)


person5('Jack', 24, job='Engineer')

# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：


# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)


# 通过一个tuple和dict，你也可以调用上述函数：
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)


# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。


# 递归函数
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017268131039072
# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


print(fact(1))
print(fact(5))
print(fact(100))


# ===> fact(5)
# ===> 5 * fact(4)
# ===> 5 * (4 * fact(3))
# ===> 5 * (4 * (3 * fact(2)))
# ===> 5 * (4 * (3 * (2 * fact(1))))
# ===> 5 * (4 * (3 * (2 * 1)))
# ===> 5 * (4 * (3 * 2))
# ===> 5 * (4 * 6)
# ===> 5 * 24
# ===> 120


# 递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。

# 使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，
# 栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。

# 解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

def fact1(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact1(5))
# ===> fact_iter(5, 1)
# ===> fact_iter(4, 5)
# ===> fact_iter(3, 20)
# ===> fact_iter(2, 60)
# ===> fact_iter(1, 120)
# ===> 120


# 使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
# 针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。
# Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。


def moveHanNuo(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        moveHanNuo(n-1, a, c, b)
        moveHanNuo(1, a, b, c)
        moveHanNuo(n-1, b, a, c)


moveHanNuo(3, 'A', 'B', 'C')
