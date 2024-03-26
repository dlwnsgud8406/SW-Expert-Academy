import sys
sys.stdin = open("input.txt", "r")

length = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr[length//2])

