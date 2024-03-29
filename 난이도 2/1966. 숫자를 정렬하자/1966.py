import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    print("#{}".format(test_case), *arr)
