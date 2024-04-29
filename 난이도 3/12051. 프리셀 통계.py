import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

T = int(input())
for test_case in range(T):
    n, Pd, Pg = map(int, input().split())

    if Pd != 0 and Pg == 0 :
        print('#%d %s' % (test_case, 'Broken'))
    elif Pd != 100 and Pg == 100 :
        print('#%d %s' % (test_case, 'Broken'))
    else :
        flag = False
        for i in range(1, n + 1) :
            if (i * Pd) / 100 == (i * Pd) // 100 : # 정수라면
                flag = True
                break

        if flag :
            print('#%d %s' % (test_case, 'Possible'))
        else :
            print('#%d %s' % (test_case, 'Broken'))
