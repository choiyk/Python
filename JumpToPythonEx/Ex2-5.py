# 연습문제 2-5
# coding=utf-8

# 1
print("#1")
a = {'name': '홍길동', 'birth': '1128', 'age': '30'}
print(a)

# 2
print("#2")
a = dict()
a['name'] = 'python'
a[('a',)] = 'python'
# a[[1]] = 'python' 리스트는 변하는 값
a[250] = 'python'
print(a)
# ※ Key에는 변하지 않는 값을 사용하고, Value에는 변하는 값과 변하지 않는 값 모두 사용할 수 있다.

# 3
print("#3")
a = {'A': 90, 'B': 80, 'C': 70}
print(a['B'])
del a['B']
# a.pop('B')
print(a)

# 4
print("#4")
a = {'A': 90, 'B': 80}
print(a.get('C', 70))

# 5
print("#5")
a = {'A': 90, 'B': 80, 'C': 70}
a1 = list(a.values())
a1.sort()
print(a1[0])
print(min(a.values()))

# 6
print("#6")
a = {'A': 90, 'B': 80, 'C': 70}
a1 = list(a.items())
a1.sort()
print(a1)