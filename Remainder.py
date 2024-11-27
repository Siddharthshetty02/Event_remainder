import csv
from datetime import datetime, timedelta
import time
from plyer import notification

EVENT_FILE = "events.csv"

def add_event():
    """Add a new event to the CSV file."""
    title = input("Enter event title: ")
    description = input("Enter event description (optional): ")
    date = input("Enter event date (YYYY-MM-DD): ")
    time_ = input("Enter event time (HH:MM, 24-hour format): ")

    try:
        # Validate date and time format
        datetime.strptime(date, "%Y-%m-%d")
        datetime.strptime(time_, "%H:%M")

        # Save the event
        with open(EVENT_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([title, description, date, time_])
        print("Event added successfully!")
    except ValueError:
        print("Invalid date or time format. Please try again.")

def view_events():
    """Display all scheduled events."""
    try:
        with open(EVENT_FILE, "r") as file:
            reader = csv.reader(file)
            events = list(reader)

        if not events:
            print("No events found.")
        else:
            print("\nScheduled Events:")
            print(f"{'Title':<20}{'Description':<30}{'Date':<15}{'Time':<10}")
            print("-" * 75)
            for event in events:
                print(f"{event[0]:<20}{event[1]:<30}{event[2]:<15}{event[3]:<10}")
    except FileNotFoundError:
        print("No events found. Start by adding some events.")

def check_reminders():
    """Check if any event is due and send a notification."""
    while True:
        try:
            with open(EVENT_FILE, "r") as file:
                reader = csv.reader(file)
                events = list(reader)

            now = datetime.now()
            for event in events:
                event_time = datetime.strptime(f"{event[2]} {event[3]}", "%Y-%m-%d %H:%M")
                time_diff = event_time - now

                # Notify if the event is due within the next minute
                if timedelta(0) <= time_diff <= timedelta(minutes=1):
                    notification.notify(
                        title=f"Reminder: {event[0]}",
                        message=f"{event[1]}",
                        timeout=10
                    )
                    print(f"Reminder: {event[0]} - {event[1]}")
                    time.sleep(60)  # Prevent duplicate notifications

            time.sleep(10)  # Check for reminders every 10 seconds
        except FileNotFoundError:
            print("No events found. Start by adding some events.")
            break

def main():
    while True:
        print("\nEvent Reminder")
        print("1. Add Event")
        print("2. View Events")
        print("3. Start Reminder")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_event()
        elif choice == "2":
            view_events()
        elif choice == "3":
            print("Checking for reminders...")
            check_reminders()
        elif choice == "4":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
