import datetime

# Your input dates
input_checkin_date = "2024-11-19"
input_checkout_date = "2024-11-21"

# Convert the input dates to datetime objects at midnight UTC
date1 = datetime.datetime.strptime(input_checkin_date, "%Y-%m-%d").replace(tzinfo=datetime.timezone.utc, hour=0, minute=0, second=0, microsecond=0)
date2 = datetime.datetime.strptime(input_checkout_date, "%Y-%m-%d").replace(tzinfo=datetime.timezone.utc, hour=0, minute=0, second=0, microsecond=0)

# Convert the datetime objects to timestamps in milliseconds
checkin_timestamp = int(date1.timestamp() * 1000)
checkout_timestamp = int(date2.timestamp() * 1000)

print(f"checkin date in millis is --> {checkin_timestamp}")
print(f"checkout date in millis is --> {checkout_timestamp}")
