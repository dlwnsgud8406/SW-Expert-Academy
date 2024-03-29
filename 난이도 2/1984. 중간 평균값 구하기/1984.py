import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    arr = sorted(list(map(int, input().split())))[1:9]
    print("#{} {}".format(test_case, round(sum(arr) / len(arr))))


