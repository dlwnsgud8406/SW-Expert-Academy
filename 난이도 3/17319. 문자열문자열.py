import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    length = int(input())
    string = input()
    if string[:length // 2] == string[length//2:]:
        print("#{} {}".format(test_case, "Yes"))
    else:
        print("#{} {}".format(test_case, "No"))


