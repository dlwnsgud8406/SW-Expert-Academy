import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

T = int(input())
for test_case in range(T):
    D, L, N = map(int, input().split())
    answer = 0
    for i in range(0, N):
        answer += (D * (1 + i * L * 0.01))
    print("#{} {}".format(test_case+1, int(answer)))
