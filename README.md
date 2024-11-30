# Event Reminder

A Python-based event reminder application to schedule and notify users about important events.

## Features
- Add events with details (title, description, date, and time).
- View all scheduled events.
- Receive desktop notifications when an event is due.

## Requirements
- Python 3.x
- Install dependencies:

## How to Use
1. Clone or download the repository.
2. Navigate to the project folder:
3. Run the script:
4. Use the menu to:
- Add events.
- View events.
- Start reminders.

## File Structure
event-reminder/ ├── reminder.py # Main script ├── events.csv # CSV file to store event data ├── README.md # Project description and instructions

## Notes
- Events are stored in a `CSV` file. Ensure you do not delete or modify it manually.
- The reminder checks for events due within a minute and sends a notification.
  
## Enhancements
GUI Integration:
Use Tkinter or PyQt to create a graphical interface for adding and viewing events.
Email Reminders:
Integrate email notifications using the smtplib library.
Recurring Events:
Add support for recurring events (e.g., daily, weekly, monthly).
Advanced Storage:
Use a database (e.g., SQLite) instead of a CSV file for better scalability.

## SIDDHARTH RAGHUNATHA SHETTY
Developer and Maintainer
