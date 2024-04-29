import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

T = int(input())
for test_case in range(T):
    num = int(input())
    answer = 0
    arr = list(map(int, input().split()))
    for i in range(1, num-1):
        if arr[i] != max(arr[i-1:i+2]) and arr[i] != min(arr[i-1:i+2]):
            answer += 1
    print("#{} {}".format(test_case+1, answer))
