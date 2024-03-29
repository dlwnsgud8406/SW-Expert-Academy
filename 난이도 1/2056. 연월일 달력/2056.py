def is_valid_date(month, day):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return day <= 31
    elif month == 2:
        return day <= 29
    else:
        return day <= 30


T = int(input())
for test_case in range(1, T + 1):
    board = input()
    year, month, day = int(board[:4]), int(board[4:6]), int(board[6:8])

    year_str = f"{year:04d}"
    month_str = f"{month:02d}"
    day_str = f"{day:02d}"

    if month < 1 or month > 12 or day < 1 or day > 31:
        print(f"#{test_case} -1")
    elif not is_valid_date(month, day):
        print(f"#{test_case} -1")
    else:
        print(f"#{test_case} {year_str}/{month_str}/{day_str}")
