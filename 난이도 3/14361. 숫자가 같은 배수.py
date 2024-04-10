import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")
from collections import Counter
T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    string_num = str(num)
    answer = 'impossible'
    for i in range(2, 10):
        if Counter(string_num) == Counter(str(num * i)):
            answer = 'possible'
    print("#{} {}".format(test_case, answer))
