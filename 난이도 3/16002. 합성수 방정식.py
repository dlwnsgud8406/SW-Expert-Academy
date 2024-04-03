import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    num1, num2 = N * 9, N * 8
    print("#{} {} {}".format(test_case, num1, num2))
