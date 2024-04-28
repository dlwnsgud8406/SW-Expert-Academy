import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    firstDayList = []

    for i in range(len(A)):
        if A[i] == 1:
            firstDayList.append(i)

    answer = 1e9

    for day in firstDayList:
        dayCnt = 0
        classCnt = 0
        while classCnt < N:
            if A[day] == 1:
                classCnt += 1
            dayCnt += 1
            if day > 5:
                day = 0
            else:
                day += 1
        answer = min(answer, dayCnt)

    print("#{} {}".format(test_case + 1, answer))
