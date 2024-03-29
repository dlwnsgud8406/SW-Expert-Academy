import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    answer = 0
    string = sorted(list(input()))
    string = ''.join(string)
    for i in range(len(string)):
        for j in range(len(string)-i):
            # print(string[j:j+i+1])
            if string[j:j+i+1] == string[j:j+i+1][::-1]:
                answer += 1
    print("#{} {}".format(test_case, answer))
