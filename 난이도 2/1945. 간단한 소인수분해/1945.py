import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    prime_list = [2,3,5,7,11]
    count_list = [0,0,0,0,0]
    for i in range(5):
        while n % prime_list[i] == 0:
            count_list[i] += 1
            n //= prime_list[i]
    print("#{}".format(test_case), *count_list)
