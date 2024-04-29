T = int(input())

for test_case in range(1, T + 1) :
    p = input().rstrip()
    q = input().rstrip()

    if p + "a" != q :
        print('#%d %s' % (test_case, 'Y'))
    else :
        print('#%d %s' % (test_case, 'N'))
