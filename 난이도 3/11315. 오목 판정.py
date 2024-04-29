import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

def search_win(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'o':
                for di, dj in ((1, 0), (0, 1), (1, 1), (1, -1)):
                    ci = i
                    cj = j
                    cnt = 0
                    while 0 <= ci <= N-1 and 0 <= cj <= N-1 and board[ci][cj] == 'o':
                        cnt += 1
                        ci += di
                        cj += dj
                    if cnt >= 5:
                        return 'YES'
    return 'NO'

T = int(input())
for test_case in range(T):
    N = int(input())
    board = list(input() for _ in range(N))

    print("#{} {}".format(test_case+1, search_win(board)))
