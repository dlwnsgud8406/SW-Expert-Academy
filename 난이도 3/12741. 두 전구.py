import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

T = int(input())
answer_list = []
for test_case in range(T):
    A, B, C, D = map(int, input().split())
    if A > C:
        A, B, C, D = C, D, A, B
    if B < C:
        answer = 0
    elif B >= D:
        answer = D - C
    elif D > B and B >= C:
        answer = B - C
    answer_list.append(answer)
for i in range(T):
    print("#{} {}".format(i + 1, answer_list[i]))
