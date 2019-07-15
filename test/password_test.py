import unittest
from src import utility

class PasswordTest(unittest.TestCase):

    def test_for_checking_length_of_returned_password(self):
        length_list = [4,6,8]
        list_of_passwords = utility.generate_password(length_list)
        self.assertEqual(len(list_of_passwords), 3)


if __name__ == '__main__':
    unittest.main()