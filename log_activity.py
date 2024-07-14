import os
import getpass
from datetime import datetime

log_file = "user_activity.log"

def log_event(event):
    username = getpass.getuser()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as file:
        file.write(f"{current_time} - {username} - {event}\n")

if __name__ == "__main__":
    log_event("Login")
    print("Press Enter to log out...")
    input()
    log_event("Logout")