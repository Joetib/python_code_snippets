import time

def countdown_timer(seconds):
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

# Example usage: countdown_timer(10)
# Output: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, Time's up!

# Please Like and Subscribe