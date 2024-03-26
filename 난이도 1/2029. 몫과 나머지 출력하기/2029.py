import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    a, b = max(a, b), min(a, b)
    print("#{} {} {}".format(test_case, a//b, a%b))
