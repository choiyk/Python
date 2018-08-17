# 연습문제 2-2
# coding=utf-8

# 1
print("#1")
print('"점프 투 파이썬" 문제를 풀어보자')

# 2
print("#2")
print("""
Life is too short
You need Python
""")

# 3
print("#3")
s = "PYTHON"
print(" " * 24 + s)

# 4
print("#4")
pin = "881120-1068234"
print(pin[:6])
print(pin[7:])

# 5
print("#5")
pin = "881120-1068234"
print(pin[7])

# 6
print("#6")
s = "1980M1120"
s = s[4] + s[:4] + s[5:]
print(s)

# 7
print("#7")
s = "PYTHON"
print("%30s" % s)
print("{0:>30}".format(s))

# 8
print("#8")
s = "Life is too short, you need python"
print(s.find('short'))

# 9
print("#9")
s = "a:b:c:d"
print(s.replace(':', '#'))

# 10
print("#10")
s = "a:b:c:d"
s = s.split(":")
a = "#"
b = a.join(s)
print(b)
# ※ join을 이용한 문자열 삽입은 문자열 뿐만 아니라 리스트에도 사용 가능하다.

