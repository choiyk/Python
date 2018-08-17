from copy import deepcopy
#연습문제 2-8
#coding=utf-8

#1
print("#1")
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)   #False : 각 변수가 가리키는 매모리의 주소가 다름
print(id(a))
print(id(b))

#2
print("#2")
a = [1, 2, 3]
b = a
print(a is b)   #True : 변수가 가리키는 메모리의 주소가 같다
print(id(a))
print(id(b))

#3
print("#3")
a = b = [1, 2, 3]
a[1] = 4
print(b)
#b[1] 도 4로 바뀐다 : a와 b가 같은 메모리 주소를 가리키기 때문
#a = [1, 2, 3]
#b = a 과 같다
print(id(a))
print(id(b))

#4
print("#4")
a = [1, 2, 3]
b = a[:]
print(a is b)   #False : a와 b의 메모리 주소가 다르며 b = a[:]은 a를 복사한것과 같다

#5
print("#5")
a = [1, 2, 3]
b = a[:]
a[1] = 4
print(b)    #a=[1,4,3] b=[1,2,3]

#6
print("#6")
a = [1, 2, 3]
print(id(a))
a = a + [4,5]
print("+연산: "+str(id(a)))
#a=[1, 2, 3, 4, 5]
a = [1, 2, 3]
print(id(a))
a.extend([4, 5])
print("extend: "+str(id(a)))
#a=[1, 2, 3, 4, 5]

#7
print("#7")
a = [1, [2, 3], 4]
b = a[:]
a[1][0] = 5
#a=[1, [5, 3], 4]
print(b)    #b=[1,[5,3],4] : b = a[:]는 2depth 이상의 리스트는 copy하지 못함

a = [1, [2, 3], 4]
b = deepcopy(a)
a[1][0] = 5
#a=[1, [5, 3], 4]
print(b)


