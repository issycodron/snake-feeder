'''
Script that runs the functions in feeder.py
'''

# Import necessary modules
from datetime import date
from feeder import log_feeding, read_last_feeding_date, next_feeding_date, days_since_feeding, calculate_urgency_score, get_status_updates
from display import display_status, display_urgency

# run feeder.py here. initial testing

if __name__ == "__main__":
    last_feeding = read_last_feeding_date()
    if last_feeding:
        status = get_status_updates()
        display_status(status)
        days_since = days_since_feeding(last_feeding)
        urgency_score = calculate_urgency_score(days_since)
        display_urgency(urgency_score, days_since)
    else:
        print("No feeding data found.")




