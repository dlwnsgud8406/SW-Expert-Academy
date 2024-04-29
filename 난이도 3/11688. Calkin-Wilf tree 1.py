T = int(input())

for test_case in range(1, T + 1) :
    n = input()
    a, b = 1, 1

    for value in n :
        if value == 'L' :
            b = a + b
        elif value == 'R' :
            a = a + b

    print('#{} {} {}'.format(test_case, a, b))
