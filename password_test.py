import unittest
from src.utility import generate_password


class PasswordTest(unittest.TestCase):
    def test_for_checking_length_of_returned_password_list(self):
        length_list = [4, 6, 8]
        list_of_passwords = generate_password(length_list)
        self.assertEqual(len(list_of_passwords), 3)

    def test_each_password_is_of_given_length(self):
        length_list = [4, 7, 5]
        list_of_passwords = generate_password(length_list)
        for i in range(len(length_list)):
            self.assertEqual(len(list_of_passwords[i]), length_list[i])


if __name__ == "__main__":
    unittest.main()
