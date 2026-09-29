import os

ATTENDANCE_FILE = "data/attendance.txt"


def mark_attendance():
    member_id = input("Enter member ID: ")
    date = input("Enter date (DD-MM-YYYY): ")

    file = open(ATTENDANCE_FILE, "a")
    file.write(member_id + "|" + date + "\n")
    file.close()

    print("Attendance marked successfully.")


def view_attendance():
    if not os.path.exists(ATTENDANCE_FILE):
        print("No attendance records found.")
        return

    file = open(ATTENDANCE_FILE, "r")
    found = False

    print("\n--- ATTENDANCE RECORDS ---")
    for line in file:
        line = line.strip()
        if line != "":
            parts = line.split("|")
            print("Member ID:", parts[0], "Date:", parts[1])
            found = True

    file.close()

    if not found:
        print("No attendance records found.")
