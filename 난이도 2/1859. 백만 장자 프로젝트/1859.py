import sys
sys.stdin = open("input.txt", "r")


T = int(input())
# for test_case in range(0, T):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     answer = 0
#     current_max = 0
#     bought_list = []
#     for i in range(n):
#         if i + 1 == n or arr[i] > arr[i+1]:
#             current_max = arr[i]
#             if len(bought_list) != 0 and current_max > bought_list[0] :
#                 answer += ((current_max * len(bought_list)) - sum(bought_list))
#             bought_list.clear()
#             current_max = 0
#         else:
#             current_max = max(current_max, arr[i])
#             bought_list.append(current_max)
#
#     print('#{} {}'.format(test_case+1, answer))

# T = int(input())
# for test_case in range(0, T):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     answer = 0
#     sellPrice = 0
#
#     for val in arr[::-1]:
#         if val >= sellPrice:
#             sellPrice = val
#         else:
#             answer += sellPrice - val
#     print("#", test_case+1, " ", answer, sep="")
for test_case in range(0, T):
    n = int(input())
    maps = list(map(int , input().split()))
    tot = 0
    while len(maps) != 0:
        idx_max = max(maps)
        now = maps.index(idx_max)

        imci = maps[:now]
        maps = maps[now+1:]

    for i in range(len(imci)):
        tot += abs(imci[i] - idx_max)
    print(f"#{test_case} {tot}")
