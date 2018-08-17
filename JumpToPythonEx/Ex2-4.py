# 연습문제 2-4
# coding=utf-8

# 1
print("#1")
t = (3,)  # 1개의 요소값을 가지는 튜플은 항상 콤마를 포함해 주어야 한다.
print(t)

# 2
print("#2")
print("튜플은 값을 지우거나 변경할 수 없음")

# 3
print("#3")
t = (1, 2, 3)
a = (4,)
b = t + a
print(b)
