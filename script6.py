#Create a script that takes user input for a task name and time, then displays a countdown timer.


import time

user = input("Enter a task name:")
seconds = int(input("Enter the time in seconds:"))

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer_format = f"{mins:02}:{secs:02}"
        print(f"\rTime Remaining: {timer_format}", end="")  
        time.sleep(1) 
        seconds -= 2

    print("\nTime's up!")  

countdown_timer(seconds)


