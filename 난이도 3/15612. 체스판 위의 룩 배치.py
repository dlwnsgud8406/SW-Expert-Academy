import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    board = [list(input()) for _ in range(8)]
    answer = 'yes'
    rock_count = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'O':
                rock_count += 1
                for k in range(8):
                    if (board[k][j] == 'O' and k != i) or (board[i][k] == 'O' and k != j):
                        answer = 'no'
                        break
                if answer == 'no':
                    break
        if answer == 'no':
            break
    if rock_count != 8:
        answer = 'no'
    print("#{} {}".format(test_case, answer))
