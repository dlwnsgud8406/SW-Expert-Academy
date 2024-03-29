import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    size = int(input())

    board = []
    for i in range(size):
        board.append(list(map(int,input().split())))
    print("#%d" %test_case)

    for i in range(size):
        for j in range(size):
            print(board[size-1-j][i],end='')
        print(end=' ')
        for j in range(size):
            print(board[size-1-i][size-1-j],end='')
        print(end=' ')
        for j in range(size):
            print(board[j][size-1-i],end='')
        print()
