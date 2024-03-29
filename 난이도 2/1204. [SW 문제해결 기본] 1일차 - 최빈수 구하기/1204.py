from collections import Counter

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    num_counter = Counter(arr)
    print("#{} {}".format(n, num_counter.most_common(1)[0][0]))
