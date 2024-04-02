import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    if a == b:
        answer = a
    else:
        answer = 1
    print("#{} {}".format(test_case, answer))
