'''
feeder.py
Core logic for the snake feeding tracker.
Handles state saving, time calculations, and urgency scoring.
'''

import json
from datetime import date, timedelta
from pathlib import Path

def get_data_file_path():
    """
    Returns the path to the snake_state.json file.
    """
    return Path(__file__).resolve().parent.parent / 'data' / 'snake_state.json'


def log_feeding(feeding_date):
    """
    Logs a feeding event by saving the provided feeding_date to a JSON file.

    Args:
        feeding_date (date): The date of the feeding event as a datetime.date object.
    """
    data_file = get_data_file_path()

    # Create a dictionary with the feeding date
    data = {'last_feeding': feeding_date.isoformat()}

    # Write the dictionary to the JSON file
    with open(data_file, 'w') as f:
        json.dump(data, f, indent=2)


def read_last_feeding_date():
    """
    Reads the last feeding date from the JSON file.

    Returns:
        date: The last feeding date as a datetime.date object, or None if not found.
    """
    data_file = get_data_file_path()

    if not data_file.exists():
        return None  # No feeding data found

    try:
        with open(data_file, 'r') as f:
            data = json.load(f)
            last_feeding_str = data.get('last_feeding')
            if last_feeding_str:
                return date.fromisoformat(last_feeding_str)
    except json.JSONDecodeError:
        # Handle corrupted or invalid JSON file
        return None

    return None  # No valid feeding date found

def next_feeding_date(last_feeding_date, days_between_feedings=5):
    """
    Calculates the next feeding date based on the last feeding date.

    Args:
        last_feeding_date (date): The date of the last feeding event as a datetime.date object.
        days_between_feedings (int): The number of days between feedings.

    Returns:
        date: The calculated next feeding date.
    """
    # For example, if the snake needs to be fed every 7 days
    return last_feeding_date + timedelta(days=days_between_feedings)


def days_since_feeding(last_feeding_date):
    """
    Calculates the number of days since the last feeding date.

    Args:
        last_feeding_date (date): The date of the last feeding event as a datetime.date object.

    Returns:
        int: The number of days since the last feeding.
    """
    return (date.today() - last_feeding_date).days

def calculate_urgency_score(days_since_last_feeding, days_between_feedings=5):
    """
    Calculates an urgency score based on the number of days since the last feeding.
    Day 0 - 0/5 = 0.0 not urgent
    Day 5 - 5/5 = 1.0 urgent
    in between - 0.2, 0.4, 0.6, 0.8. 
    0-0.4 is not urgent, 0.6 is starting to get urgent, 0.8 is get ready, and 1 is urgent.
    day 6 is 6/5 = 1.2, which is should come as urgent plus a warning message
    day 7 is 7/5 = 1.4, which is very urgent and should come with an urgent warning message.

    Args:
        days_since_last_feeding (int): The number of days since the last feeding.
        days_between_feedings (int): The number of days between feedings.

    Returns:
        float: An urgency score where 0 means not urgent and higher values indicate more urgency.
    """
    # firstly, calculate the base urgency score as a ratio of days since last feeding to days between feedings
    urgency_score = days_since_last_feeding / days_between_feedings
    
    # i want continuous scale for LED implementation, so return the calculated urgency score instead of discrete categories
    return urgency_score
    







