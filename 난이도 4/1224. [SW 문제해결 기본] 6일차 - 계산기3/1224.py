import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    n = int(input())
    answer = eval(input())
    print("#{} {}".format(test_case, answer))
