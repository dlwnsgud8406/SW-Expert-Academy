import sys
sys.stdin = open("input.txt", "r")

num = input()
answer = 0
for n in num:
    answer += int(n)
print(answer)

