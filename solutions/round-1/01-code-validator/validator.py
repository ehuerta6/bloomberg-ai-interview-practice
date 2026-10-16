import unittest


def is_valid_access_code(code):
    """Return True only for a six-character string of ASCII digits."""
    return (
        isinstance(code, str)
        and len(code) == 6
        and all("0" <= character <= "9" for character in code)
    )


class ValidatorTests(unittest.TestCase):
    def test_six_ascii_digits_are_valid(self):
        self.assertTrue(is_valid_access_code("123456"))

    def test_leading_zeroes_are_preserved(self):
        self.assertTrue(is_valid_access_code("001234"))

    def test_wrong_length_is_invalid(self):
        for code in ("", "12345", "1234567"):
            with self.subTest(code=code):
                self.assertFalse(is_valid_access_code(code))

    def test_non_ascii_or_non_digit_characters_are_invalid(self):
        for code in ("12a456", "１２３４５６", "١٢٣٤٥٦", "12 456"):
            with self.subTest(code=code):
                self.assertFalse(is_valid_access_code(code))

    def test_non_string_values_are_invalid_without_raising(self):
        for code in (123456, None, ["1", "2"]):
            with self.subTest(code=code):
                self.assertFalse(is_valid_access_code(code))


if __name__ == "__main__":
    unittest.main()
