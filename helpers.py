from datetime import datetime, date


def get_user_input(prompt):
    return input(prompt).strip()


def str_to_datetime(date_str, time_str):
    return datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")


def get_date_input():
    today = date.today()
    while True:
        date_str = get_user_input("Enter date (YYYY-MM-DD): ")
        try:
            input_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            if input_date < today:
                print(
                    "Error: The date cannot be in the past. Please enter a future date."
                )
            else:
                return date_str
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")


def get_time_input():
    while True:
        time_str = get_user_input("Enter time (HH:MM): ")
        try:
            datetime.strptime(time_str, "%H:%M")
            return time_str
        except ValueError:
            print("Invalid time format. Please use HH:MM.")


def verify_date_time(date_str, time_str):
    today = datetime.now()
    input_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    if input_datetime < today:
        return False
    return True
