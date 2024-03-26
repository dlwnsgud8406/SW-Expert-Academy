import sys
sys.stdin = open("input.txt", "r")

n = int(input())
answer = []

for i in range(1, int(n ** (1 / 2)) + 1):
    if n % i == 0:
        answer.append(i)
        if i < n // i:
            answer.append(n // i)
answer.sort()
print(*answer)
