import unittest
import sys
sys.path.append(".")

from member import Member


class TestGymManagement(unittest.TestCase):

    def test_member_creation(self):
        member = Member("M01", "Rahul", 20, "9876543210", "Monthly")
        self.assertEqual(member.name, "Rahul")
        self.assertEqual(member.plan, "Monthly")

    def test_member_id(self):
        member = Member("M02", "Anita", 21, "9876500000", "Yearly")
        self.assertEqual(member.member_id, "M02")


if __name__ == "__main__":
    unittest.main()
