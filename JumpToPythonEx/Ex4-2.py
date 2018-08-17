#연습문제 4-2
#coding=utf-8

#1
print("#1")
input1 = int(input("첫번째 숫자를 입력하세요: "))
input2 = int(input("두번째 숫자를 입력하세요: "))
total = input1 + input2
print("두 수의 합은 %s입니다." % total)

#2
print("#2")
nums = input()
nums = nums.split(",")
sum = 0
for num in nums:
    sum += int(num)
print(sum)

#4
print("#4")
num = int(input("구구단을 출력할 숫자를 입력하세요(2~9): "))
for i in range(1, 10):
    print(i*num, end=" ")
