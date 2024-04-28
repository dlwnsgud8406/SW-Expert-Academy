import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

T = int(input())
for test_case in range(T):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    board = [0, 0, 0, 0]

    for col in range(n):
        for row in range(m):
            if arr[col][row] == '#':
                if (col+row) % 2 == 0:
                    board[0] += 1
                elif (col+row) % 2 == 1:
                    board[1] += 1
            elif arr[col][row] == '.':
                if (col + row) % 2 == 0:
                    board[2] += 1
                elif (col + row) % 2 == 1:
                    board[3] += 1
    if (board[0] and board[1]) or (board[2] and board[3]) or (board[0] and board[2]) or (board[1] and board[3]):
            answer = 'impossible'
    else:
            answer = 'possible'

    print(f"#{test_case + 1}", answer)

