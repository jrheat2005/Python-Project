import datetime
import pytz

# Time zone definitions
portland_tz = pytz.timezone('America/Los_Angeles')
nyc_tz = pytz.timezone('America/New_York')
london_tz = pytz.timezone('Europe/London')

# Get current times
current_time_portland = datetime.datetime.now(portland_tz)
current_time_nyc = datetime.datetime.now(nyc_tz)
current_time_london = datetime.datetime.now(london_tz)

# Branch hours
branch_open_time = datetime.time(9, 0)    # 9:00 a.m.
branch_close_time = datetime.time(17, 0)  # 5:00 p.m.

# Function to check if a branch is open
def is_branch_open(current_time):
    return branch_open_time <= current_time.time() <= branch_close_time

# Check and print branch status
print("Portland HQ is", "open" if is_branch_open(current_time_portland) else "closed")
print("New York City branch is", "open" if is_branch_open(current_time_nyc) else "closed")
print("London branch is", "open" if is_branch_open(current_time_london) else "closed")
