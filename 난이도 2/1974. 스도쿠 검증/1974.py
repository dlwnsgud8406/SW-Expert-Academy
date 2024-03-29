import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    board = []
    for _ in range(9):
        row = list(map(int, input().split()))
        board.append(row)
    answer = 1
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if board[i][j] == board[i][k] and j != k:
                    answer = 0
                    break

            for l in range(9):
                if board[i][j] == board[l][j] and i != l:
                    answer = 0
                    break

            for m in range(i//3*3, i//3*3+3):
                for n in range(j//3*3, j//3*3+3):
                    if board[i][j] == board[m][n] and (i != m or j != n):
                        answer = 0
                        break

    print("#{} {}".format(test_case, answer))
