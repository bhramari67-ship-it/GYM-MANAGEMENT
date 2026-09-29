from member import Member

FILE_NAME = "data/members.txt"


def load_members():
    members = []
    try:
        file = open(FILE_NAME, "r")
        for line in file:
            line = line.strip()
            if line != "":
                parts = line.split("|")
                if len(parts) == 5:
                    member = Member(parts[0], parts[1], parts[2], parts[3], parts[4])
                    members.append(member)
        file.close()
    except FileNotFoundError:
        pass
    return members


def save_members(members):
    file = open(FILE_NAME, "w")
    for member in members:
        line = member.member_id + "|" + member.name + "|" + str(member.age)
        line = line + "|" + member.phone + "|" + member.plan + "\n"
        file.write(line)
    file.close()


def add_member(members):
    member_id = input("Enter member ID: ")
    for member in members:
        if member.member_id == member_id:
            print("This member ID already exists.")
            return

    name = input("Enter member name: ")
    age = input("Enter age: ")
    phone = input("Enter phone number: ")
    plan = input("Enter plan (Monthly/Quarterly/Yearly): ")

    member = Member(member_id, name, age, phone, plan)
    members.append(member)
    save_members(members)
    print("Member added successfully.")


def view_members(members):
    if len(members) == 0:
        print("No members found.")
        return

    print("\n--- GYM MEMBERS ---")
    for member in members:
        print(member.member_id, "-", member.name, "-", member.plan)


def search_member(members):
    member_id = input("Enter member ID to search: ")
    for member in members:
        if member.member_id == member_id:
            member.show_details()
            return
    print("Member not found.")


def remove_member(members):
    member_id = input("Enter member ID to remove: ")
    for member in members:
        if member.member_id == member_id:
            members.remove(member)
            save_members(members)
            print("Member removed.")
            return
    print("Member not found.")
