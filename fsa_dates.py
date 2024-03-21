def validate_date(date_string):
    try:
        day, month, year = map(int, date_string.split('/'))
        if len(date_string) != 10 or date_string[2] != '/' or date_string[5] != '/' or not (1 <= month <= 12) or not (1 <= day <= 31):
            return False
        if month in [4, 6, 9, 11] and day > 30:
            return False
        if month == 2:
            if day > 29:
                return False
            if day == 29 and (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0)):
                return False
        return True
    except ValueError:
        return False


# Test the DateValidator
test_dates = ["31/12/2022", "29/02/2024", "12/06/1990", "30/02/2025", "11/13/2023"]

for date in test_dates:
    if validate_date(date):
        print(f"{date} is a valid date.")
    else:
        print(f"{date} is not a valid date.")
