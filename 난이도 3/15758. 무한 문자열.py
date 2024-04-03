import sys

sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

import math
T = int(input())
for test_case in range(1, T + 1):
    S, T = input().split(' ')
    answer = ''
    gcd = math.gcd(len(S), len(T))
    lcm = (len(S) // gcd) * (len(T) // gcd) * gcd
    if (S * (lcm // len(S))) == (T * (lcm // len(T))):
        answer = 'yes'
    else:
        answer = 'no'
    print("#{} {}".format(test_case, answer))
