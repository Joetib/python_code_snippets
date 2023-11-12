# To create a calendar reminder in Python, we can use the `schedule` library.
# Install the `schedule` library using:
# >> pip install schedule

import schedule
import time

def reminder():
    print("It's time for your reminder!")

# Schedule the reminder to run every day at 9:00 AM
schedule.every().day.at("09:00").do(reminder)

# Keep the program running indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)

# Output:
# It's time for your reminder!
# It's time for your reminder!
# It's time for your reminder!
# ... (continues running every day at 9:00 AM)
# Please Like and Subscribe