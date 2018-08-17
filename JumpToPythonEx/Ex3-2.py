#연습문제 3-2
#coding=utf-8

#1
print("#1")
i = 1
s = 0
while i <= 100:
    s = s + i
    i = i + 1
print(s)

#2
print("#2")
i = 1
s = 0
while i <= 1000:
    if i % 3 == 0:
        s = s + i
    i = i + 1
print(s)

#3
print("#3")
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
i = 0
s = 0
while i < len(A):
    if A[i] >= 50:
        s += A[i]
    i += 1
print(s)

s1 = 0
while A:
    score = A.pop();
    if score >= 50:
        s1 += score
print(s1)

#4
print("#4")
i = 1
while i < 5:
    print("*"*i)
    i += 1

#5
print("#5")
i = 7
j = 0
while j < 5:
    print(" "*j+"*"*i)
    j += 1
    i -= 2
