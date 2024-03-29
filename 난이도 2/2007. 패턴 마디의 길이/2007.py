import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    string = input()
    char = string[-1]
    index_list = []
    for i, v in enumerate(string):
        if v == char:
            index_list.append(i)
    print("#{} {}".format(test_case, index_list[-1] - index_list[-2]))
