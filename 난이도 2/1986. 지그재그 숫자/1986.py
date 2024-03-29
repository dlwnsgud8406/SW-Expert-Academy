import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    answer = 0
    n = int(input())
    for i in range(1, n+1):
        if i % 2 == 1:
            answer += i
        else:
            answer -= i
    print("#{} {}".format(test_case, answer))
