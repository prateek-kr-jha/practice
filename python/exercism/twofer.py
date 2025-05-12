import unittest


class TwoFerTest(unittest.TestCase):
    def test_no_name_given(self):
        self.assertEqual(two_fer(), "One for you, one for me.")
    def test_a_name_given(self):
        self.assertEqual(two_fer("Alice"), "One for Alice, one for me.")
    def test_another_name_given(self):
        self.assertEqual(two_fer("Bob"), "One for Bob, one for me.")


def two_fer(name="you"):
    
    return  f"One for {name}, one for me."

test = TwoFerTest()

test.test_a_name_given()
test.test_another_name_given()
test.test_no_name_given()