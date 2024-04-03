import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    board = input()
    answer = 0
    idx = 0
    while idx < len(board):
        if board[idx] =='(':
            if board[idx+1] == ')':
                answer += 1
                idx += 1
            else:
                answer += 1
        elif board[idx] == ')':
            answer += 1
        idx += 1
    print("#{} {}".format(test_case, answer))
