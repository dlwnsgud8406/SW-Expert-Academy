import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    a_hour, a_minute, b_hour, b_minute = map(int, input().split())
    answer_hour, answer_minute = a_hour + b_hour, a_minute + b_minute
    if answer_minute >= 60:
        answer_minute -= 60
        answer_hour += 1
    if answer_hour > 12:
        answer_hour -= 12
    print("#{} {} {}".format(test_case, answer_hour, answer_minute))

