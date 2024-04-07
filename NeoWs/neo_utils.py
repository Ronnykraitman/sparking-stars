from datetime import datetime


def get_dates_by_user_for_neo():
    is_diff_ok = False
    start_date = ""
    end_date = ""
    print("Neo supports searching in a 7 days range\n")
    while not is_diff_ok:
        start_date = get_date_from_user("Please enter the start date (YYYY-MM-DD): ")
        end_date = get_date_from_user("Please enter the end date (YYYY-MM-DD): ")
        is_diff_ok = check_neo_dates_diff(start_date, end_date)

    return start_date, end_date


def get_date_from_user(msg: str):
    date = input(msg)
    is_ok = check_neo_date_format(date)
    while not is_ok:
        start_date = input("Wrong date format. Please re - enter the date (YYYY-MM-DD): ")
        is_ok = check_neo_date_format(start_date)
    return date

def check_neo_date_format(date):
    date_format = "%Y-%m-%d"
    try:
        datetime.strptime(date, date_format)
        return True
    except ValueError:
        return False

def check_neo_dates_diff(start, end):
    date_format = "%Y-%m-%d"
    start_date = datetime.strptime(start, date_format)
    end_date = datetime.strptime(end, date_format)
    if (end_date - start_date).days > 7:
        print("Neo can only check 7 days at one time. Please select different range of dates")
        return False
    else:
        return True
