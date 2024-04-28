import sys
sys.stdin = open("/Users/ijunhyeong/Desktop/코딩테스트 대비/SW-Expert-Academy/input.txt", "r")

T = int(input())
for test_case in range(T):
    game = input()
    if game.count('x') >= 8:
        answer = 'NO'
    else:
        answer = 'YES'
    print("#{} {}".format(test_case+1, answer))
