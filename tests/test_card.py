import unittest

from bank.account import Account

DEBUG=False

class CardTest(unittest.TestCase):
    def setUp(self):
        self.acc = Account(name="John", surname="Doe")

    def test_basic(self):
        # given
        card = self.acc.create_new_card(4321)

        # when
        owner = card.owner

        # then
        self.assertEquals(owner, self.acc.owner)

    def test_check_pin(self):
        # given
        pin = 12345
        card = self.acc.create_new_card(pin)

        # when
        is_pin_ok = card.check_pin(pin)

        # then
        self.assertTrue(is_pin_ok)

    def test_get_account(self):
        # given
        pin = 12345
        card = self.acc.create_new_card(pin)

        # when
        account = card.get_account()

        # then
        self.assertEqual(account, self.acc)

    @unittest.expectedFailure
    def test_is_pin_number(self):
        # given
        pin = 'abc12345'
        card = self.acc.create_new_card(pin)

        # when
        is_pin_ok = card.is_pin_number()

        # then
        self.assertTrue(is_pin_ok)

