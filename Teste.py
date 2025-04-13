from datetime import datetime, timedelta

def Calendar():
    # Get today's date
    todayy = datetime.today()

    # Set the start date (January 1st of the current year)
    start_date =datetime(todayy.year,todayy.month,todayy.day-1)
    end_datee = datetime(todayy.year,todayy.month,todayy.day)
    print(datetime(todayy.year,todayy.month,todayy.day-1))
    print(end_datee)
    # Loop through each day from the start date to today
    current_date = start_date
    end_date = end_datee



Calendar()