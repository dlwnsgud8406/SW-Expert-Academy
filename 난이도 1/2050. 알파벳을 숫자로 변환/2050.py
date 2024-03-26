import sys
sys.stdin = open("input.txt", "r")

answer = []

string = input()
for char in string:
    answer.append((ord(char) + 1) % 65)
print(*answer)
