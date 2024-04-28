import sys
from collections import deque
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")


def bfs():
    len_shap_xy = len(shap_xy) ** 0.5

    if len_shap_xy % 1 != 0:  # 정사각형이 이루어질 수 있는 개수(1, 4, 9 ...)가 아님
        return "no"

    x, y = shap_xy.popleft()
    for i in range(x, x + int(len_shap_xy)):
        for j in range(y, y + int(len_shap_xy)):
            if pan[i][j] == '.':
                return "no"
    return "yes"

T = int(input())
for test_case in range(T):
    N = int(input())
    pan = [deque(input()) for _ in range(N)]
    shap_xy = deque()
    for i in range(N):
        for j in range(N):
            if pan[i][j] == '#':
                shap_xy.append((i, j))
    answer = bfs()

    print(f"#{test_case + 1}", answer)
