'''
Script that runs the functions in feeder.py
'''

# Import necessary modules
from datetime import date
from feeder import log_feeding, read_last_feeding_date, next_feeding_date

# run feeder.py here. initial testing

if __name__ == "__main__":
    # Example usage: log a feeding event with today's date
    log_feeding(date.today())
    #did it work? print something to confirm
    print("Feeding event logged for today's date.")

# call read_last_feeding_date to see if it returns the correct date
if __name__ == "__main__":
    last_feeding = read_last_feeding_date()
    if last_feeding:
        print(f"Last feeding date: {last_feeding}")
    else:
        print("No feeding data found.")

# call next_feeding_date to see if it calculates the next feeding date correctly

if __name__ == "__main__":
    last_feeding = read_last_feeding_date()
    if last_feeding:
        next_feeding = next_feeding_date(last_feeding)
        print(f"Next feeding date: {next_feeding}")
    else:
        print("No feeding data found. Cannot calculate next feeding date.")