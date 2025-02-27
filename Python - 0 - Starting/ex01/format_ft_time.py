import time
import datetime

timestamp = time.time()

print(f"Seconds since January 1, 1970: {timestamp:,.4f} or {timestamp:.2e} in scientific notation")

current_date = datetime.datetime.now()

formatted_date = current_date.strftime("%b %d %Y")
print(formatted_date)