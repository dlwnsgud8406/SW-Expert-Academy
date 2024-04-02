import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    answer = 0
    for i in range(N, -N-1, -1):
        for j in range(N, -N-1, -1):
            if i**2 + j**2 <= N ** 2:
                answer += 1
    print("#{} {}".format(test_case, answer))
