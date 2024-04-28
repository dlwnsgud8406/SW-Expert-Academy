import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    answer = 10000000009
    for i in range(N-K+1):
        answer = min(answer, max(arr[i:K+i]) - min(arr[i:K+i]))
    print("#{} {}".format(test_case, answer))
