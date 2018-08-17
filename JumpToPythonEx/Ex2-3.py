# 연습문제 2-3
# coding=utf-8

# 1
print("#1")
a = ['Life', 'is', 'too', 'short', 'you', 'need', 'python']
print(a[4] + " " + a[2])

# 2
print("#2")
a = ['Life', 'is', 'too', 'short']
s = " ".join(a)
print(s)

# 3
print("#3")
a = [1, 2, 3]
print(len(a))

# 4
print("#4")
a = [1, 2, 3]
a.append([4, 5])  # [1, 2, 3, [4, 5]] 리스트 뒤에 요소 붙이기
print(a)
a.extend([4, 5])  # [1, 2, 3, 4, 5] 리스트를 확장
print(a)

# 5
print("#5")
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# 6
print("#6")
a = [1, 2, 3, 4, 5]
a.remove(2)
del a[2]
print(a)
# a.remove(x) - x는 a리스트의 요소값
# a.pop(x) - x는 a리스트의 인덱스
# del a[x] - x는 a리스트의 인덱스