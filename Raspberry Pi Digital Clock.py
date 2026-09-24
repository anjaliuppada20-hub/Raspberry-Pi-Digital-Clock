import time
from datetime import datetime

def digital_clock():
    print("Raspberry Pi Digital Clock")
    print("Press Ctrl+C to exit.\n")

    try:
        while True:
            current_time = datetime.now().strftime("%H:%M:%S")
            current_date = datetime.now().strftime("%d-%m-%Y")

            print(f"\rDate: {current_date}   Time: {current_time}", end="", flush=True)

            time.sleep(1)

    except KeyboardInterrupt:
        print("\n\nClock stopped.")


if __name__ == "__main__":
    digital_clock()
