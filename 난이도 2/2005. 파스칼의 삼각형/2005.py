import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    pascal = [[0] * n for _ in range(n)]
    pascal[0][0] = 1
    for i in range(1, n):
        for j in range(n):
            if j == 0:
                pascal[i][j] = 1
            else:
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    print('#{}'.format(test_case))
    for k in range(n):
        for l in range(n):
            if pascal[k][l]:
                print(pascal[k][l], end=' ')
        print()

