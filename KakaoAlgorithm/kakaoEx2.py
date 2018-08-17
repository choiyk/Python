#카카오 문제 2
#coding=utf-8

def devideStr(str):
    arr = []
    index = 0
    for i in range(len(str)):
        if str[i] == 'S' or str[i] == 'D' or str[i] == 'T':
            arr.append(str[index:i])
            arr.append(str[i])
            index = i+1
            if str[i+1] != '#' and str[i+1] != '*':
                arr.append(" ")
        elif str[i] == '#' or str[i] == '*':
            arr.append(str[i])
            index = i+1
    return arr

def star(n, score):
    for i in range(n//2):
        score[i] *= 2
    return score

def sharp(n, score):
    score[(n // 2) - 1] *= -1
    return score

def score(arr):
    score = []
    for i in range(len(arr)):
        if arr[i] == 'S':
            score.append(int(arr[i-1]))
        elif arr[i] == 'D':
            score.append(pow(arr[i-1], 2))
        elif arr[i] == 'T':
            score.append(pow(arr[i-1], 3))
        elif arr[i] == '*':
            score = star(i, score)
        elif arr[i] == '#':
            score = sharp(i, score)

    return sum(score)



a = "1T2D3D#"
arr = devideStr(a)
print(arr)
#print(score(arr))