from datetime import datetime

def get_days_from_today(date):
    start_date = datetime.strptime(date, "%Y-%m-%d")
    end_date = datetime.today()
    return end_date - start_date

try:
    input_date = input("Enter your date 'YYYY-MM-DD': ")
    today_date = datetime.today().date()
    print(f"Today`s date: {today_date}  \nDays between dates: {get_days_from_today(input_date).days}")
except ValueError:
    print("Invalid date, does not match format 'YYYY-MM-DD'. Try again.")