#연습문제 5-1
#coding=utf-8

#1
print("#1")
class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val

cal = Calculator()
cal.add(3)
cal.add(4)

print(cal.value)

#2
print("#2")
class Calculator2:
    def __init__(self, init_value=0):
        self.value = init_value

    def add(self, val):
        self.value += val

cal = Calculator2()
cal.add(3)
cal.add(4)

print(cal.value)

#3
print("#3")
class Calculator3:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator3):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)  # 10에서 7을 뺀 3을 출력

#4
print("#4")
class MaxLimitCalculator(Calculator3):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50)  # 50 더하기
cal.add(60)  # 60 더하기

print(cal.value)  # 100 출력

#5
print("#5")
class Calculator4:
    def __init__(self, list):
        self.list = list
        self.total = 0
    def sum(self):
        for val in self.list:
            self.total += val
        return self.total
    def avg(self):
        return self.total / len(self.list)

cal1 = Calculator4([1,2,3,4,5])
print(cal1.sum())  # 15 출력
print(cal1.avg())  # 3.0 출력

cal2 = Calculator4([6,7,8,9,10])
print(cal2.sum())  # 40 출력
print(cal2.avg())  # 8.0 출력
