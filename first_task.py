from datetime import datetime

def get_days_from_today(date):
    try:
        start_date = datetime.strptime(date, "%Y-%m-%d")
        end_date = datetime.today()
        return (end_date - start_date).days
    except ValueError:
        print("Invalid date, does not match format 'YYYY-MM-DD'. Try again.")
        return None

input_date = input("Enter your date 'YYYY-MM-DD': ")
today_date = datetime.today().date()
days_diff = get_days_from_today(input_date)
if days_diff is not None:
    print(f"Today`s date: {today_date}  \nDays between dates: {days_diff}")
