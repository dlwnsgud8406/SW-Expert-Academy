n = int(input())

answer = [1, ]
value = 1
for i in range(1, n+1):
    value *= 2
    answer.append(value)
print(*answer)
