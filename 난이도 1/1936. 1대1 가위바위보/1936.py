import sys
sys.stdin = open("input.txt", "r")

a, b = map(int, input().split())
if a - b == -1 or a - b == 2:
    print('B')
elif a - b == 1 or a - b == -2:
    print('A')
