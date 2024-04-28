import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    a,b = map(int,input().split())
    diff = b-a
    if diff == 0:
        answer = 0
    elif diff <= 1:
        answer = -1
    elif diff % 2 == 0:
        answer = diff // 2
    else:
        answer = (diff - 3) // 2 + 1
    print(f'#{test_case} {answer}')
