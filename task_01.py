""" define diffference between current and predefined dates """



from datetime import date, datetime
import re


## SCENARIO 1 - catch an exception:

# def get_days_from_today(date: str) -> int:
#     try:
#         date_obj = datetime.strptime(date, "%Y-%m-%d").date()
#     except Exception:
#         print("the date should be given in the format: YYYY-MM-DD")
#     else:
#         today = datetime.today().date()
#         days_diff = date_obj - today

#         return days_diff.days


## SCENARIO 2 - raise an exception:

def get_days_from_today(date: str) -> int:
    match_format = re.match(r"\d{4}-\d{2}-\d{2}", date)
    if match_format:
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()   
        today = datetime.today().date()
        days_diff = date_obj - today

        return days_diff.days
    else:
        raise ValueError("the date should be given in the format: YYYY-MM-DD")

date_delta = get_days_from_today("2024-07-01")
print(date_delta)