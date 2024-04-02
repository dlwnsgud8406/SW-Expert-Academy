import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    answer = 0
    dist2 = arr[2] - arr[1]
    dist1 = arr[1] - arr[0]
    if dist2 == dist1:
        answer = 0
    elif dist1 > dist2:
        answer = (dist1 - dist2) / 2
    else:
        answer = (dist2 - dist1) / 2
    print("#{}".format(test_case),end=' ')
    print(format(answer, ".1f"))
