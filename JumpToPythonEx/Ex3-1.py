#연습문제 3-1
#coding=utf-8

#1
print("#1")
money = 5000
card = False
if card or money >= 4000:
    print("택시를 탈 수 있습니다.")
else:
    print("택시를 탈 수 없습니다.")

#2
print("#2")
lucky_list = [1, 9, 23, 46]
lucky = 23
if lucky in lucky_list:
    print("야호")
else:
    print("당첨되지 않았습니다.")

#3
print("#3")
num = 3
if num%2 == 1: print("홀수")
else: print("짝수")

#4
print("#4")
s = "나이:30,키:180"
s1 = s.split(",") #['나이:30', '키:180']
age = int(s1[0].split(":")[1])
tall = int(s1[1].split(":")[1])
if age < 30 and tall >= 175:
    print("YES")
else:
    print("NO")

#5
print("#5")
a = "Life is too short, you need python"
if 'wife' in a:
    print('wife')
elif 'python' in a and 'you' not in a:
    print('python')
elif 'shirt' not in a:
    print('shirt')
elif 'need' in a:
    print('need')
else:
    print('none')
#shirt
