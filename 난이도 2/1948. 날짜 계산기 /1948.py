import sys
sys.stdin = open("input.txt", "r")
month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

T = int(input())

for test_case in range(1, T+1):
    ans = 0
    small_month, small_day, big_month, big_day = map(int, input().split())
    if small_month == big_month:
        ans = big_day - small_day
    else:
        for i in range(small_month, big_month+1):
            if i == small_month:
                ans += (month[i] - small_day)
            elif i == big_month:
                ans += big_day
            else:
                ans += month[i]
    print('#{} {}'.format(test_case, ans+1))
