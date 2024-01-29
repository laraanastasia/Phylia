from datetime import datetime, timedelta

def first_monday_dates(year):
    first_mondays = []

    for month in range(1, 13):
        # Find the first day of the month
        first_day = datetime(year, month, 1)
        
        # Calculate the difference to the first Monday
        days_to_monday = (7 - first_day.weekday() ) % 7
        
        # Calculate the date of the first Monday
        first_monday = first_day + timedelta(days=days_to_monday)
        
        first_mondays.append(first_monday)

    return first_mondays

# Example usage:
year = 2024
first_mondays = first_monday_dates(year)

for first_monday in first_mondays:
    print(f"The first Monday of {first_monday.strftime('%B %Y')} is on {first_monday.strftime('%Y-%m-%d')}")
