import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

T = int(input())
for test_case in range(T):
    num = input()
    answer_min = num
    answer_max = num
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            change_num = num[:i] + num[j] + num[i+1:j] + num[i] + num[j+1:]
            if change_num[0] != '0':
                answer_min = min(answer_min, change_num)
            answer_max = max(answer_max, change_num)

    print("#{} {} {}".format(test_case+1, answer_min, answer_max))
