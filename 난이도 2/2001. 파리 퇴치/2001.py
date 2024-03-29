import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    answer = 0
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            sub_matrix_sum = sum(arr[x][y] for x in range(i, i + m) for y in range(j, j + m))
            answer = max(answer, sub_matrix_sum)

    print("#{} {}".format(test_case, answer))
