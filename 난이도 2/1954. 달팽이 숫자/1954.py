import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [[ 4*i*(n-i) + (1+x+y - 2*i if (x==i or y==n-i-1) else (4*n - 6*i - x - y -3))  for i,x,y in row]   for row in [[(min(n-x-1,x,n-y-1,y),x,y) for y in range(n)] for x in range(n)]]
    print("#{}".format(test_case))
    for row in arr:
        print(*row)
