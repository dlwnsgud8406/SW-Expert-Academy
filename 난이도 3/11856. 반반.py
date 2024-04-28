import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

T = int(input())
for test_case in range(T):
    string = input()
    is_half_state = True
    for char in string:
        if string.count(char) != 2:
            is_half_state = False
            break
    if is_half_state:
        print("#{} {}".format(test_case + 1, 'Yes'))
    else:
        print("#{} {}".format(test_case + 1, 'No'))
