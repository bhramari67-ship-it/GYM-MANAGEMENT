import os


def show_summary(members):
    print("\n--- GYM SUMMARY ---")
    print("Total members:", len(members))

    monthly = 0
    quarterly = 0
    yearly = 0

    for member in members:
        if member.plan.lower() == "monthly":
            monthly = monthly + 1
        elif member.plan.lower() == "quarterly":
            quarterly = quarterly + 1
        elif member.plan.lower() == "yearly":
            yearly = yearly + 1

    print("Monthly plans:", monthly)
    print("Quarterly plans:", quarterly)
    print("Yearly plans:", yearly)

    if os.path.exists("data/payments.txt"):
        file = open("data/payments.txt", "r")
        total = 0
        for line in file:
            line = line.strip()
            if line != "":
                parts = line.split("|")
                total = total + float(parts[1])
        file.close()
        print("Total payments:", total)
    else:
        print("Total payments: 0")
