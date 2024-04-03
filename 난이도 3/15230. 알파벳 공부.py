import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

T = int(input())
compare_string = 'abcdefghijklmnopqrstuvwxyz'
for test_case in range(1, T + 1):
    string = input()
    answer = 0
    for i in range(len(string)):
        if compare_string[i] == string[i]:
            answer += 1
        else:
            break
    print("#{} {}".format(test_case, answer))
