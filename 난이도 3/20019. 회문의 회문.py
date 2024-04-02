import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    string = input()
    length = len(string)
    needed_size = (length-1) // 2
    if string == string[::-1] and string[:needed_size] == string[-needed_size:]:
        print("#{} {}".format(test_case, "YES"))
    else:
        print("#{} {}".format(test_case, "NO"))
