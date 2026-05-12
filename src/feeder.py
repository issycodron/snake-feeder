'''
feeder.py
Core logic for the snake feeding tracker.
Handles state saving, time calculations, and urgency scoring.
'''

import json
from datetime import date
from pathlib import Path

def log_feeding(feeding_date):
    """
    Logs a feeding event by saving the provided feeding_date to a JSON file.

    Args:
        feeding_date (date): The date of the feeding event as a datetime.date object.
    """
    # Determine the path to the data/snake_state.json file
    data_file = Path(__file__).resolve().parent.parent / 'data' / 'snake_state.json'

    # Create a dictionary with the feeding date
    data = {'last_feeding': feeding_date.isoformat()}

    # Write the dictionary to the JSON file
    with open(data_file, 'w') as f:
        json.dump(data, f, indent=2)




