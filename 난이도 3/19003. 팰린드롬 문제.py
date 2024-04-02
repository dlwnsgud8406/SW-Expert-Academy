import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    answer1 = 0
    answer2 = 0
    string_list = []
    for _ in range(N):
        tmp_s = input()
        string_list.append(tmp_s)
    for string in string_list:
        if string[::-1] in string_list and string != string[::-1]:
            answer1 += M
        elif string[::-1] in string_list:
            answer2 = M
    answer = answer1 + answer2
    print('#{} {}'.format(test_case, answer1 + answer2))
