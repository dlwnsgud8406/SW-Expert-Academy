import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    answer = ''
    for i in range(n):
        char, num = input().split(' ')
        answer += (char * int(num))
    length = len(answer) // 10
    idx = 0
    print("#{}".format(test_case))
    for idx in range(length):
        print(answer[idx * 10 :(idx+1) * 10])
    print(answer[(idx+1) * 10: len(answer) + 1]  )
