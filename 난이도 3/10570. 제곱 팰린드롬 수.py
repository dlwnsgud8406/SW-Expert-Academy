import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

T = int(input())
for test_case in range(T):
    a, b = map(int, input().split())
    answer = 0
    for i in range(a, b+1):
        if (i**0.5) == int(i**0.5) and str(i) == str(i)[::-1] and str(int(i**0.5)) == str(int(i**0.5))[::-1] :
            answer += 1
    print("#{} {}".format(test_case, answer))
