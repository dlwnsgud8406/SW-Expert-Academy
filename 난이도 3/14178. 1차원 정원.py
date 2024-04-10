import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")
import math
T = int(input())
for test_case in range(1, T + 1):
    N, D = map(int, input().split())
    water_distance = 2 * D + 1
    answer = math.ceil(N/water_distance)
    print("#{} {}".format(test_case, answer))
