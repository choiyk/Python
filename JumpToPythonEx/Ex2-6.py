# 연습문제 2-6
# coding=utf-8

#1
print("#1")
a = set(['a', 'b', 'c'])
print(a)

#2
print("#2")
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
a1 = set(a)
b = list(a1)
print(b)

#3
print("#3")
s1 = set(['a', 'b', 'c', 'd', 'e'])
s2 = set(['c', 'd', 'e', 'f', 'g'])
s3 = s1-s2
print(s3)

#4
print("#4")
a = set()
print(type(a))

#5
print("#5")
a = {'a', 'b', 'c'}
b = {'d', 'e', 'f'}
a.update(b)
print(a)

