import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

T = int(input())
for test_case in range(T):
    print("#{} {}".format(test_case + 1, sum(map(int, input().split())) % 24))
