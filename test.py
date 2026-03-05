import calendar

# Take year as input
year = int(input("Enter the year: "))

# Print the calendar for the given year
print("\nCalendar for the year", year)
print(calendar.calendar(year))
