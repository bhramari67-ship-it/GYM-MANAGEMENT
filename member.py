class Member:
    def __init__(self, member_id, name, age, phone, plan):
        self.member_id = member_id
        self.name = name
        self.age = age
        self.phone = phone
        self.plan = plan

    def show_details(self):
        print("ID:", self.member_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Phone:", self.phone)
        print("Plan:", self.plan)
