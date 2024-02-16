import unittest


def validate_email_address(email):
    if "@" in email and "." in email.split("@")[1]:
        return True
    return False

class TestValidateEmailAddress(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(validate_email_address("example@example.com"))
        self.assertTrue(validate_email_address("user.name+tag+sorting@example.com"))
        self.assertTrue(validate_email_address("x@example.com"))
        self.assertTrue(validate_email_address("example-indeed@strange-example.com"))

    def test_invalid_email(self):
        self.assertFalse(validate_email_address("plainaddress"))
        self.assertFalse(validate_email_address("@missingusername.com"))
        self.assertFalse(validate_email_address("Joe Smith <email@example.com>"))
        self.assertFalse(validate_email_address("email.example.com"))
        self.assertFalse(validate_email_address("email@example@example.com"))
        self.assertFalse(validate_email_address(".email@example.com"))
        self.assertFalse(validate_email_address("email.@example.com"))
        self.assertFalse(validate_email_address("email..email@example.com"))
        self.assertFalse(validate_email_address("あいうえお@example.com"))
        self.assertFalse(validate_email_address("email@example.com (Joe Smith)"))
        self.assertFalse(validate_email_address("email@-example.com"))
        self.assertFalse(validate_email_address("email@example..com"))

if __name__ == '__main__':
    unittest.main()
