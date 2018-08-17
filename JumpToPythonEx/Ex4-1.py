#연습문제 4-1
#coding=utf-8

#1
print("#1")
def is_odd(num):
    result = num % 2
    if result == 1:
        print("홀수")
    else:
        print("짝수")

is_odd(3)
is_odd(4)

#2
print("#2")
def avg(*args):
    sum = 0
    for i in args:
        sum += i
    return sum / len(args)

print(avg(1,2,3,4,5,6,7,8,9,10))

#3
print("#3")
def googoodan(num):
    for i in range(1, 10):
        print(f"{num}X{i}={num * i}")

googoodan(8)

#4
print("#4")
def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)

print(fib(3))

#5
print("#5")
myfunc = lambda numbers: [number for number in numbers if number > 5]
print(myfunc([2,3,4,5,6,7,8]))