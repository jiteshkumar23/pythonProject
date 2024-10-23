import datetime

from config import checkInDate, checkOutDate

# Your input dates in the format YYYY-MM-DD
input_checkin_date = checkInDate
input_checkout_date = checkOutDate

# Convert the input dates to datetime objects at midnight UTC
date1 = datetime.datetime.strptime(input_checkin_date, "%Y-%m-%d").replace(tzinfo=datetime.timezone.utc, hour=0,
                                                                           minute=0, second=0, microsecond=0)
date2 = datetime.datetime.strptime(input_checkout_date, "%Y-%m-%d").replace(tzinfo=datetime.timezone.utc, hour=0,
                                                                            minute=0, second=0, microsecond=0)

# Convert the datetime objects to timestamps in milliseconds
checkin_timestamp = int(date1.timestamp() * 1000)
checkout_timestamp = int(date2.timestamp() * 1000)

print(f"checkin date {input_checkin_date} converted to millis is --> {checkin_timestamp}")
print(f"checkout date {input_checkout_date} converted to  millis is --> {checkout_timestamp}")