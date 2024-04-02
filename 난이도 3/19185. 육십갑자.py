import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    return a * b // gcd(a, b)

T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    LCM = lcm(n,m)
    s = list(map(str, input().split()))
    t = list(map(str, input().split()))
    year_list = []
    for i in range(LCM):
        year_list.append(s[i % n] + t[i % m])

    answer = []
    Q = int(input())
    for _ in range(Q):
        year = int(input())
        answer.append(year_list[year % LCM -1])

    print("#{} {}".format(test_case, ' '.join(answer)))
