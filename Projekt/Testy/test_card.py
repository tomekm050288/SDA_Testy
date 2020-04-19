import unittest
from Bank import Account
from faker import Faker

DEBUG = False


class CardTest(unittest.TestCase):

    def setUp(self) -> None:
        Faker.seed(0)
        self.acc = Account("John", "Doe")

    def test_basic(self):
        # given
        card = self.acc.create_card("4567")

        # when
        owner = card.card_owner

        #then
        self.assertEqual(owner, self.acc.owner())

    def test_check_pin(self):
        # given
        pin = '1235'
        card = self.acc.create_card("1235")

        # when
        is_pin_ok = card.check_pin(pin)

        #then
        self.assertTrue(is_pin_ok)

    def test_get_account(self):
        # given
        pin = '1235'
        card = self.acc.create_card("1235")

        # when
        number = card.get_account()

        # then
        self.assertEqual(number, str(self.acc))

    @unittest.expectedFailure
    def test_ispin_number(self):
        # given
        pin = 'aaa1235'
        card = self.acc.create_card("1235")

        # when
        is_pin_ok = card.check_pin(pin)

        #then
        self.assertTrue(is_pin_ok)
