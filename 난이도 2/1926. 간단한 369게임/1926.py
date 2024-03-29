import sys
sys.stdin = open("input.txt", "r")

n = int(input())
answer = ''
for i in range(1, n+1):
    num = str(i)
    if '3' in num or '6' in num or '9' in num:
        answer += (num.count('3') + num.count('6') + num.count('9')) * '-'
    else:
        answer += num
    answer += ' '
print(answer[:-1])
