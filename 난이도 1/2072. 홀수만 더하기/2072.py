import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    arr = list(map(int, input().split()))
    answer = 0
    for num in arr:
        if num % 2 == 1:
            answer += num
    print('#{} {}'.format(test_case, answer))
    # ///////////////////////////////////////////////////////////////////////////////////
