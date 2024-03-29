import sys
sys.stdin = open("input.txt", "r")

T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    score_list = []
    for _ in range(N):
        mid, final, hw = map(int, input().split())
        score = (mid * 0.35) + (final * 0.45) + (hw * 0.2)
        score_list.append(score)

    k_score = score_list[K - 1]

    score_list.sort(reverse=True)

    div = N // 10
    k_percentage = score_list.index(k_score) // div

    print('#{} {}'.format(test_case, grade[k_percentage]))

