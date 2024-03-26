answer = ''

string = input()

for char in string:
    if char.islower():
        answer += char.upper()
    else:
        answer += char
print(answer)
