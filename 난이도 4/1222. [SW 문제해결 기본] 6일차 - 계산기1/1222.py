import sys
sys.stdin = open("input.txt", "r")

for i in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split('+')))
    print("#{} {}".format(i, sum(arr)))
