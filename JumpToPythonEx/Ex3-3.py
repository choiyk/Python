#연습문제 3-3
#coding=utf-8

#1
print("#1")
for i in range(1, 101):
    print(i, end=" ")

#2
print("#2")
s = 0
for i in range(1, 1001):
    if i % 5 == 0:
        s += i
print(s)

#3
print("#3")
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
s = 0
for a in A:
    s += a
ave = s / len(A)
print(ave)

#4
print("#4")
blood_data = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
blood = {'A': 0, 'B': 0, 'O': 0, 'AB': 0}
for b in blood_data:
    if b == 'A':
        blood['A'] += 1
    elif b == 'B':
        blood['B'] += 1
    elif b == 'O':
        blood['O'] += 1
    elif b == 'AB':
        blood['AB'] += 1
print(blood)

blood2 = {}
for b in blood_data:
    if b in blood2:
        blood2[b] += 1
    else:
        blood2[b] = 1
print(blood2)

#5
print("#5")
numbers = [1, 2, 3, 4, 5]

result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)

result2 = [n for n in numbers if n % 2 == 1]
print(result2)

#6
print("#6")
short = "Life is too short, you need python"
result = [s for s in short if s not in ('a', 'e', 'i', 'o', 'u')]
#['L', 'f', ' ', 's', ' ', 't', ' ', 's', 'h', 'r', 't', ',', ' ', 'y', ' ', 'n', 'd', ' ', 'p', 'y', 't', 'h', 'n']
result2 = ""
for s in result:
    result2 += s
print(result2)

result3 = ''.join(result)
print(result3)
