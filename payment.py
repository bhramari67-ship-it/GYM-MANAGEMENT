import os

PAYMENT_FILE = "data/payments.txt"


def add_payment():
    member_id = input("Enter member ID: ")

    try:
        amount = float(input("Enter payment amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return

    date = input("Enter payment date (DD-MM-YYYY): ")

    file = open(PAYMENT_FILE, "a")
    file.write(member_id + "|" + str(amount) + "|" + date + "\n")
    file.close()

    print("Payment saved successfully.")


def view_payments():
    if not os.path.exists(PAYMENT_FILE):
        print("No payment records found.")
        return

    file = open(PAYMENT_FILE, "r")
    total = 0

    print("\n--- PAYMENT RECORDS ---")
    for line in file:
        line = line.strip()
        if line != "":
            parts = line.split("|")
            print("Member ID:", parts[0], "| Amount:", parts[1], "| Date:", parts[2])
            total = total + float(parts[1])

    file.close()
    print("Total payment received:", total)
