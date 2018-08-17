#연습문제 4-3
#coding=utf-8

#1
print("#1")
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())

#2
print("#2")
f = open("test.txt", 'a')
while 1:
    data = input("저장할 내용을 입력하세요: ")
    f.write(data+"\n")
    if not data: break
f.close()

#3
print("#3")
f = open("abc.txt", 'r')
lines = f.readlines()
'''
text = []
for line in lines:
    text.append(line)
'''
f.close()
'''
rlines = reversed(lines)
for line in rlines:
    print(line)
'''
f = open("abc.txt", 'w')
while lines:
    f.write(lines.pop())
f.close()

#4
print("#4")
f = open("test.txt", 'r')
lines = f.readlines()
f.close()
s = ''
for line in lines:
    s += line.replace('java', 'python')
f = open("test.txt", 'w')
f.write(s)
f.close()

#5
print("#5")
f = open("sample.txt", 'r')
lines = f.readlines()
f.close()
sum = 0
count = 0
for line in lines:
    sum += int(line)
    count += 1
avg = sum / count
#avg = sum / len(lines)
f = open("result.txt", 'w')
f.write(str(avg))
