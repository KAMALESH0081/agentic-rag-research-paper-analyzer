import os
from datetime import datetime

LOG_FILE = "data/log/debug_log.txt"

def log(text):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")

def log_section(title):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write("\n" + "="*50 + "\n")
        f.write(f"{title}\n")
        f.write("="*50 + "\n")

def clear_log():
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write(f"Log started at {datetime.now()}\n")