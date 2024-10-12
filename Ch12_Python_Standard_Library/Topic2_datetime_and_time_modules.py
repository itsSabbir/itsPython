"""
Python Standard Library - datetime and time modules - in the Python Programming Language
========================================================================================

Table of Contents:
1. Overview and Historical Context
2. Syntax, Key Concepts, and Code Examples
3. Best Practices, Common Pitfalls, and Advanced Tips
4. Integration and Real-World Applications
5. Advanced Concepts and Emerging Trends
6. FAQs and Troubleshooting
7. Recommended Tools, Libraries, and Resources
8. Performance Analysis and Optimization
9. How to Contribute

Author: Sabbir Hossain

1. Overview and Historical Context
----------------------------------
The datetime and time modules are core components of Python's standard library, providing essential functionalities for working with dates, times, and time intervals.

Historical context:
- The time module has been part of Python since its early versions, providing low-level time-related functions.
- The datetime module was introduced in Python 2.3 (2003) to provide higher-level date and time manipulation objects.
- Both modules have undergone significant improvements over the years, with Python 3.x versions introducing new features and optimizations.

Significance:
- datetime module: Provides classes for working with dates and times at a higher level of abstraction.
- time module: Offers functions for working with times, including time conversions and sleeping.

Common use cases:
- Date and time arithmetic
- Parsing and formatting date strings
- Working with time zones
- Measuring code execution time
- Scheduling tasks and creating delays

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

import datetime
import time
from typing import List, Tuple
import zoneinfo

def demonstrate_datetime_basics():
    """Demonstrate basic usage of the datetime module."""
    # Creating datetime objects
    now = datetime.datetime.now()
    print(f"Current date and time: {now}")
    
    specific_date = datetime.datetime(2023, 1, 1, 12, 0, 0)
    print(f"Specific date and time: {specific_date}")
    
    # Date arithmetic
    tomorrow = now + datetime.timedelta(days=1)
    print(f"Tomorrow: {tomorrow}")
    
    # Formatting dates
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Formatted date: {formatted_date}")
    
    # Parsing date strings
    parsed_date = datetime.datetime.strptime("2023-01-01 12:00:00", "%Y-%m-%d %H:%M:%S")
    print(f"Parsed date: {parsed_date}")

def demonstrate_time_basics():
    """Demonstrate basic usage of the time module."""
    # Current time as a floating-point number of seconds since the epoch
    current_time = time.time()
    print(f"Current time (seconds since epoch): {current_time}")
    
    # Convert seconds since epoch to a struct_time
    time_struct = time.localtime(current_time)
    print(f"Local time: {time_struct}")
    
    # Format time
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time_struct)
    print(f"Formatted time: {formatted_time}")
    
    # Measure execution time
    start_time = time.perf_counter()
    # Simulate some work
    time.sleep(0.1)
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time:.6f} seconds")

def date_range(start_date: datetime.date, end_date: datetime.date) -> List[datetime.date]:
    """Generate a range of dates."""
    return [start_date + datetime.timedelta(days=x) for x in range((end_date - start_date).days + 1)]

def demonstrate_date_operations():
    """Demonstrate various date operations."""
    start = datetime.date(2023, 1, 1)
    end = datetime.date(2023, 1, 10)
    date_list = date_range(start, end)
    print("Date range:")
    for date in date_list:
        print(date)
    
    # Find the day of the week
    print(f"Day of the week for {start}: {start.strftime('%A')}")
    
    # Calculate age
    birthdate = datetime.date(1990, 1, 1)
    today = datetime.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    print(f"Age: {age}")

def demonstrate_timezone_handling():
    """Demonstrate handling of time zones."""
    # Create a timezone-aware datetime
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    print(f"Current UTC time: {now_utc}")
    
    # Convert to a different time zone
    ny_tz = zoneinfo.ZoneInfo("America/New_York")
    now_ny = now_utc.astimezone(ny_tz)
    print(f"Current time in New York: {now_ny}")
    
    # Create a datetime with a specific time zone
    tokyo_tz = zoneinfo.ZoneInfo("Asia/Tokyo")
    tokyo_time = datetime.datetime(2023, 1, 1, 12, 0, 0, tzinfo=tokyo_tz)
    print(f"Specific time in Tokyo: {tokyo_time}")
    
    # Convert Tokyo time to UTC
    tokyo_in_utc = tokyo_time.astimezone(datetime.timezone.utc)
    print(f"Tokyo time in UTC: {tokyo_in_utc}")

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use datetime objects for date and time manipulations instead of strings.
2. Always use timezone-aware datetime objects when working with multiple time zones.
3. Use ISO format (YYYY-MM-DD) for date representations when possible.
4. Prefer datetime.timedelta for duration calculations.

Common Pitfalls:
1. Forgetting to handle time zones, leading to incorrect time comparisons or conversions.
2. Mixing naive and aware datetime objects.
3. Incorrectly parsing date strings, especially when dealing with different locale formats.
4. Not considering daylight saving time transitions in calculations.

Advanced Tips:
1. Use datetime.timedelta for precise time duration calculations.
2. Leverage the zoneinfo module (Python 3.9+) for robust timezone handling.
3. Use datetime.datetime.combine() to create datetime objects from separate date and time components.
4. Utilize the calendar module for additional date-related functionalities.
"""

import calendar

def demonstrate_advanced_techniques():
    """Demonstrate advanced techniques with datetime and time modules."""
    # Using timedelta for precise calculations
    now = datetime.datetime.now()
    future = now + datetime.timedelta(days=30, hours=12, minutes=30)
    duration = future - now
    print(f"Duration: {duration}")
    
    # Working with the last day of the month
    year, month = 2023, 2
    _, last_day = calendar.monthrange(year, month)
    last_date = datetime.date(year, month, last_day)
    print(f"Last day of {year}-{month:02d}: {last_date}")
    
    # Combining date and time
    date_part = datetime.date(2023, 1, 1)
    time_part = datetime.time(12, 30, 0)
    combined = datetime.datetime.combine(date_part, time_part)
    print(f"Combined datetime: {combined}")
    
    # Finding the next weekday
    def next_weekday(d, weekday):
        days_ahead = weekday - d.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return d + datetime.timedelta(days=days_ahead)
    
    next_monday = next_weekday(datetime.date.today(), 0)  # 0 = Monday
    print(f"Next Monday: {next_monday}")

"""
4. Integration and Real-World Applications
------------------------------------------
The datetime and time modules are fundamental in many Python applications and frameworks:

1. Django: Uses datetime for handling database timestamps and form fields.
2. SQLAlchemy: Integrates datetime objects for database column types.
3. Pandas: Extensively uses datetime for time series data analysis.

Real-world example: A simple appointment scheduling system
"""

class Appointment:
    def __init__(self, start: datetime.datetime, duration: datetime.timedelta, description: str):
        self.start = start
        self.duration = duration
        self.description = description
    
    @property
    def end(self) -> datetime.datetime:
        return self.start + self.duration
    
    def __str__(self) -> str:
        return f"{self.description}: {self.start.strftime('%Y-%m-%d %H:%M')} - {self.end.strftime('%H:%M')}"

class Schedule:
    def __init__(self):
        self.appointments: List[Appointment] = []
    
    def add_appointment(self, appointment: Appointment) -> None:
        # Check for conflicts
        for existing in self.appointments:
            if (existing.start <= appointment.start < existing.end or
                existing.start < appointment.end <= existing.end):
                raise ValueError("Appointment conflicts with existing schedule")
        self.appointments.append(appointment)
        self.appointments.sort(key=lambda a: a.start)
    
    def get_daily_schedule(self, date: datetime.date) -> List[Appointment]:
        return [a for a in self.appointments if a.start.date() == date]

def demonstrate_real_world_application():
    """Demonstrate a real-world application using datetime module."""
    schedule = Schedule()
    
    # Add some appointments
    schedule.add_appointment(Appointment(
        datetime.datetime(2023, 6, 1, 9, 0),
        datetime.timedelta(hours=1),
        "Team Meeting"
    ))
    schedule.add_appointment(Appointment(
        datetime.datetime(2023, 6, 1, 14, 0),
        datetime.timedelta(minutes=30),
        "Client Call"
    ))
    
    # Try to add a conflicting appointment
    try:
        schedule.add_appointment(Appointment(
            datetime.datetime(2023, 6, 1, 8, 30),
            datetime.timedelta(hours=1),
            "Conflicting Meeting"
        ))
    except ValueError as e:
        print(f"Failed to add appointment: {e}")
    
    # Print daily schedule
    print("Schedule for 2023-06-01:")
    for appointment in schedule.get_daily_schedule(datetime.date(2023, 6, 1)):
        print(appointment)

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Pendulum library: A more intuitive datetime library for Python.
2. Arrow library: Offers a sensible, human-friendly approach to creating, manipulating, formatting and converting dates, times, and timestamps.
3. dateutil library: Provides powerful extensions to the standard datetime module.
"""

import pendulum
import arrow
from dateutil import parser, rrule

def demonstrate_advanced_libraries():
    """Demonstrate usage of advanced date and time libraries."""
    # Pendulum
    now = pendulum.now("Europe/Paris")
    print(f"Current time in Paris (Pendulum): {now}")
    future = now.add(years=1)
    print(f"One year from now: {future}")
    
    # Arrow
    now_arrow = arrow.now()
    print(f"Current time (Arrow): {now_arrow}")
    print(f"Current time in human-readable format: {now_arrow.humanize()}")
    
    # dateutil
    recurring_event = list(rrule.rrule(rrule.DAILY, count=5, dtstart=datetime.datetime.now()))
    print("Recurring event dates:")
    for event in recurring_event:
        print(event)

"""
6. FAQs and Troubleshooting
---------------------------
Q: How do I handle timezone-aware datetime objects?
A: Use the zoneinfo module (Python 3.9+) or pytz library for reliable timezone handling. Always create timezone-aware datetime objects when working with multiple timezones.

Q: How can I parse a date string in an unknown format?
A: The dateutil library provides a robust parser that can handle many date formats. For custom formats, use datetime.strptime() with the appropriate format string.

Q: How do I calculate the difference between two dates?
A: Use datetime.timedelta for date arithmetic. Subtract two datetime objects to get a timedelta object representing the duration.

Troubleshooting:
1. Issue: Unexpected results when comparing datetime objects
   Solution: Ensure both objects are either naive or timezone-aware. Convert naive objects to aware objects if necessary.

2. Issue: Incorrect date parsing
   Solution: Double-check the format string used in strptime(). Consider using dateutil.parser for more flexible parsing.

3. Issue: Daylight Saving Time (DST) transition issues
   Solution: Use a reliable timezone library like pytz or zoneinfo to handle DST transitions correctly.
"""

def demonstrate_troubleshooting():
    """Demonstrate common troubleshooting scenarios."""
    # Comparing naive and aware datetime objects
    naive = datetime.datetime.now()
    aware = datetime.datetime.now(datetime.timezone.utc)
    try:
        comparison = naive < aware
    except TypeError as e:
        print(f"Error comparing naive and aware datetimes: {e}")
    
    # Correct comparison
    naive_utc = naive.replace(tzinfo=datetime.timezone.utc)
    print(f"Correct comparison: {naive_utc < aware}")
    
    # Parsing ambiguous date strings
    ambiguous_date = "01-02-2023"
    try:
        parsed_mdy = datetime.datetime.strptime(ambiguous_date, "%m-%d-%Y")
        parsed_dmy = datetime.datetime.strptime(ambiguous_date, "%d-%m-%Y")
        print(f"Parsed as MDY: {parsed_mdy}")
        print(f"Parsed as DMY: {parsed_dmy}")
    except ValueError as e:
        print(f"Error parsing ambiguous date: {e}")

"""
7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
1. Pendulum: A more intuitive datetime library for Python.
2. Arrow: Simple and human-friendly date-time library.
3. dateutil: Powerful extensions to the standard datetime module.
4. pytz: Timezone definitions for Python.

Resources:
- "Python Cookbook" by David Beazley and Brian K. Jones (O'Reilly)
- "Robust Python" by Patrick Viafore (O'Reilly)
- Python's official documentation on datetime: https://docs.python.org/3/library/datetime.html
- Python's official documentation on time: https://docs.python.org/3/library/time.html
- Real Python's guide on Python datetime: https://realpython.com/python-datetime/

8. Performance Analysis and Optimization
----------------------------------------
When working with dates and times, especially in large-scale applications, performance can be a critical factor.
"""

import timeit

def performance_comparison():
    """Compare the performance of different date and time operations."""
    
    def using_datetime():
        return datetime.datetime.now()
    
    def using_time():
        return datetime.datetime.fromtimestamp(time.time())
    
    def parsing_with_strptime():
        return datetime.datetime.strptime("2023-01-01 12:00:00", "%Y-%m-%d %H:%M:%S")
    
    def parsing_with_dateutil():
        return parser.parse("2023-01-01 12:00:00")
    
    # Measure execution times
    datetime_time = timeit.timeit(using_datetime, number=100000)
    time_time = timeit.timeit(using_time, number=100000)
    strptime_time = timeit.timeit(parsing_with_strptime, number=100000)
    dateutil_time = timeit.timeit(parsing_with_dateutil, number=100000)
    
    print(f"datetime.datetime.now(): {datetime_time:.6f} seconds")
    print(f"datetime.datetime.fromtimestamp(time.time()): {time_time:.6f} seconds")
    print(f"datetime.datetime.strptime(): {strptime_time:.6f} seconds")
    print(f"dateutil.parser.parse(): {dateutil_time:.6f} seconds")

"""
Performance Considerations:
1. Creating datetime objects can be relatively expensive, especially when done frequently.
2. Parsing date strings is generally slower than working with datetime objects directly.
3. Timezone conversions can be computationally expensive, especially when dealing with daylight saving time transitions.

Optimization Strategies:
1. Cache datetime objects when possible, especially for static dates or frequently used timestamps.
2. Use datetime.datetime.fromtimestamp() instead of datetime.datetime.now() for slightly better performance when high precision is not required.
3. Prefer working with datetime objects over strings to avoid repeated parsing.
4. Use UTC for internal representations to avoid timezone conversion overhead.
"""

def optimized_date_range(start_date: datetime.date, end_date: datetime.date) -> List[datetime.date]:
    """Generate a range of dates using a more efficient method."""
    return [start_date + datetime.timedelta(days=x) for x in range((end_date - start_date).days + 1)]

def demonstrate_optimized_code():
    """Demonstrate optimized code for working with dates and times."""
    # Caching datetime objects
    epoch = datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc)
    
    def timestamp_to_datetime(ts: float) -> datetime.datetime:
        return epoch + datetime.timedelta(seconds=ts)
    
    # Measure performance
    start_time = time.perf_counter()
    for _ in range(1000000):
        dt = timestamp_to_datetime(time.time())
    end_time = time.perf_counter()
    print(f"Optimized timestamp to datetime conversion: {end_time - start_time:.6f} seconds")
    
    # Compare with standard method
    start_time = time.perf_counter()
    for _ in range(1000000):
        dt = datetime.datetime.fromtimestamp(time.time(), tz=datetime.timezone.utc)
    end_time = time.perf_counter()
    print(f"Standard timestamp to datetime conversion: {end_time - start_time:.6f} seconds")

"""
9. How to Contribute
--------------------
To contribute to this note sheet:
1. Fork the repository containing this file.
2. Make your changes or additions.
3. Ensure all code examples are correct and follow the established style.
4. Add comments explaining new concepts or functions.
5. Update the Table of Contents if necessary.
6. Submit a pull request with a clear description of your changes.

Guidelines for contributions:
- Maintain the current format and style.
- Provide working code examples for new concepts.
- Include performance considerations for new functions.
- Add relevant references or citations for advanced topics.

When adding new sections or expanding existing ones, consider the following:
- Relevance to the main topic of datetime and time modules in Python.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to datetime and time modules.
    """
    print("Demonstrating datetime basics:")
    demonstrate_datetime_basics()
    
    print("\nDemonstrating time basics:")
    demonstrate_time_basics()
    
    print("\nDemonstrating date operations:")
    demonstrate_date_operations()
    
    print("\nDemonstrating timezone handling:")
    demonstrate_timezone_handling()
    
    print("\nDemonstrating advanced techniques:")
    demonstrate_advanced_techniques()
    
    print("\nDemonstrating real-world application (appointment scheduling):")
    demonstrate_real_world_application()
    
    print("\nDemonstrating advanced libraries:")
    demonstrate_advanced_libraries()
    
    print("\nDemonstrating troubleshooting scenarios:")
    demonstrate_troubleshooting()
    
    print("\nPerformance comparison of date and time operations:")
    performance_comparison()
    
    print("\nDemonstrating optimized code:")
    demonstrate_optimized_code()

if __name__ == "__main__":
    main()