import sys
import math
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = []
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            arr.append((i, n//i))
    for i, (x, y) in enumerate(arr):
        arr[i] = (x-1)+(y-1)
    print("#{} {}".format(test_case, min(arr)))
