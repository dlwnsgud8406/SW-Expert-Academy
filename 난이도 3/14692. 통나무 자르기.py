import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    answer = ''
    if N % 2 == 0:
        answer = 'Alice'
    else:
        answer = 'Bob'
    print("#{} {}".format(test_case, answer))

