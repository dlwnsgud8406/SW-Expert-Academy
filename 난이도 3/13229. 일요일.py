import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")
week_dict = {'MON': 6, 'TUE': 5, 'WED': 4, 'THU': 3, 'FRI': 2, 'SAT': 1, 'SUN': 7}
T = int(input())
for test_case in range(T):
    print("#{} {}".format(test_case + 1, week_dict[input()]))
