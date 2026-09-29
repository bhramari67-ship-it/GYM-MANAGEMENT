from member_manager import load_members, add_member, view_members, search_member, remove_member
from attendance import mark_attendance, view_attendance
from payment import add_payment, view_payments
from report import show_summary
def show_menu():
    print("\n==============================")
    print("       GYM MANAGEMENT")
    print("==============================")
    print("1. Add member")
    print("2. View members")
    print("3. Search member")
    print("4. Remove member")
    print("5. Mark attendance")
    print("6. View attendance")
    print("7. Add payment")
    print("8. View payments")
    print("9. Show gym summary")
    print("10. Exit")
    print("==============================")

def main():
    members = load_members()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_member(members)
        elif choice == "2":
            view_members(members)
        elif choice == "3":
            search_member(members)
        elif choice == "4":
            remove_member(members)
        elif choice == "5":
            mark_attendance()
        elif choice == "6":
            view_attendance()
        elif choice == "7":
            add_payment()
        elif choice == "8":
            view_payments()
        elif choice == "9":
            show_summary(members)
        elif choice == "10":
            print("Thank you for using Gym Management.")
            break
        else:
            print("Invalid choice. Please try again.")
main()
