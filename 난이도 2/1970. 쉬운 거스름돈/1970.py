import sys
sys.stdin = open("input.txt", "r")

T = int(input())
change_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for test_case in range(1, T + 1):
    answer_coin = []
    money = int(input())
    for change in change_list:
        answer_coin.append(money // change)
        money %= change
    print("#{}".format(test_case))
    print(*answer_coin)


