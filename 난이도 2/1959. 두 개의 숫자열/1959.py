import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    answer_list = []
    size_a, size_b = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))
    if size_a > size_b:
        arr_a, arr_b = arr_b, arr_a
        size_a, size_b = size_b, size_a
    for i in range(size_b - size_a + 1):
        result = 0
        for j in range(size_a):
            result += (arr_a[j] * arr_b[i+j])
        answer_list.append(result)
    print("#{} {}".format(test_case, max(answer_list)))


