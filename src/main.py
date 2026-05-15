'''
Script that runs the functions in feeder.py
'''

# Import necessary modules
from datetime import date
from feeder import log_feeding, read_last_feeding_date, next_feeding_date, days_since_feeding, calculate_urgency_score, get_status_updates

# run feeder.py here. initial testing

if __name__ == "__main__":
    last_feeding = read_last_feeding_date()
    if last_feeding:
        status = get_status_updates()
        print(status)
        days_since = days_since_feeding(last_feeding)
        urgency_score = calculate_urgency_score(days_since)
        if urgency_score >= 1.4:
            print(f"Urgent Warning: Meeko is very hungry! Days since last feeding: {days_since}")
        elif urgency_score >= 1.2:
            print(f"Warning: Meeko is hungry! Days since last feeding: {days_since}")
    else:
        print("No feeding data found.")




