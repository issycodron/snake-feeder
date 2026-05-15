'''
Script that runs the functions in feeder.py
'''

# Import necessary modules
from datetime import date
from feeder import log_feeding, read_last_feeding_date, next_feeding_date, days_since_feeding, calculate_urgency_score, get_status_updates

# run feeder.py here. initial testing

if __name__ == "__main__":
    # Example usage: log a feeding event with today's date
    #log_feeding(date.today())
    #did it work? print something to confirm
    #print("Feeding event logged for today's date.")

# call read_last_feeding_date to see if it returns the correct date

    last_feeding = read_last_feeding_date()
    # if last_feeding:
    #     print(f"Last feeding date: {last_feeding}")
    # else:
    #     print("No feeding data found.")

# call next_feeding_date to see if it calculates the next feeding date correctly


    
    # if last_feeding:
    #     next_feeding = next_feeding_date(last_feeding)
    #     print(f"Next feeding date: {next_feeding}")
    # else:
    #     print("No feeding data found. Cannot calculate next feeding date.")

# call calculate_urgency_score to see if it returns the correct score based on the last feeding date and current date


    
    # if last_feeding:
    #     days_since = days_since_feeding(last_feeding)
    #     urgency_score = calculate_urgency_score(days_since)
    #     #print(f"Urgency score: {urgency_score:.2f}")

    # # add warning message if the score is above 1.0
    # # warning messages here until i make display functions in the future. for now, just print them out.
    # if urgency_score >= 1.4:
    #     print(f"Urgent Warning: Meeko is very hungry! Days since last feeding: {days_since}")

    # elif urgency_score >= 1.2:
    #     print(f"Warning: Meeko is hungry! Days since last feeding: {days_since}")

    # call get_status_updates to see if it returns the correct status message based on the last feeding date and current date
    status = get_status_updates()
    print(status)



else:
    print("No feeding data found. Cannot calculate urgency score.")



