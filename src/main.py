'''
Script that runs the functions in feeder.py
'''

# Import necessary modules
from datetime import date


# run feeder.py here. initial testing
from feeder import log_feeding
if __name__ == "__main__":
    # Example usage: log a feeding event with today's date
    log_feeding(date.today())
    #did it work? print something to confirm
    print("Feeding event logged for today's date.")