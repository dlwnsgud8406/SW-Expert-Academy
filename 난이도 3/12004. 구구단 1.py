arr = [i * j for i in range(1, 10) for j in range(1, 10)]
T = int(input())
for test_case in range(T):
    if int(input()) in arr:
        print("#{} {}".format(test_case + 1, 'Yes'))
    else:
        print("#{} {}".format(test_case + 1, 'No'))
