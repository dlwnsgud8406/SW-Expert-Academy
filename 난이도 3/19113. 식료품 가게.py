import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    a_list = sorted(list(map(int,input().split())), reverse=True)
    i = 0
    answer = []
    while N < len(a_list):
        if a_list[i] * 0.75 in a_list:
            tmp_i = a_list.index(a_list[i] * 0.75)
            tmp = a_list.pop(tmp_i)
            answer.append(tmp)
            i += 1
        else:
            answer.append(a_list[i])
            a_list.pop(i)
    print(f'#{testcase}', end=' ')
    for i in range(len(answer)-1, -1, -1):
        print(f'{answer[i]}', end=' ')
    print()
