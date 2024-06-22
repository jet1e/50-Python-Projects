# Countdown timer
import time, os, sys
from playsound import playsound

def countdown(t):
    for i in range(t, -1, -1):
        minutes = i // 60
        seconds = i % 60
        os.system('clear')
        if (minutes < 10) and (seconds < 10):
            print(f"0{minutes}:0{seconds}")
        elif minutes < 10:
            print(f"0{minutes}:{seconds}")
        elif seconds < 10:
            print(f"{minutes}:0{seconds}")
        else:
            print(f"{minutes}:{seconds}")
        time.sleep(1)
    blink_text("Times up!!!")
    playsound("assets/RoosterSound.wav")

def blink_text(text): # Source: https://handhikayp.medium.com/generate-a-blinking-text-with-very-simple-python-4c10750978f5#:~:text=The%20%60%5C033%5B5m%60%20sequence,the%20formatting%20back%20to%20default.
    while True:
        sys.stdout.write('\033[5m' + text + '\033[0m')
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write('\r' + ' ' * len(text) + '\r')
        sys.stdout.flush()
        time.sleep(0.5)

def main():
    try:
        t = int(input("Enter a time to countdown in seconds: "))
    except ValueError:
        print("Incorrect time")
    
    countdown(t)

main()