import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    answer = max(arr)
    print("#{} {}".format(test_case, answer))
