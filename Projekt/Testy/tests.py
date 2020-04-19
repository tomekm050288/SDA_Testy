import unittest
from Bank import Account
from faker import Faker

DEBUG = False

class AccountTest(unittest.TestCase):

    def setUp(self) -> None:
        Faker.seed(0)
        self.acc = Account("John", "Doe")

    # testy zawsze od test_

    def test_basic(self):
        acc_number = str(self.acc)
        self.assertEqual(acc_number, 'GB22VTKG87647593824219')

    def test_basic_2(self):
        Faker.seed(1)
        acc_number = str(Account("John", "Doe"))
        self.assertEqual(acc_number, 'GB42DWTG77763170669074')

    def test_owner_name(self):
        # when
        owner_name = self.acc.owner()

        # then
        self.assertEqual(owner_name, "John Doe")


    def test_balance(self):
        # when
        balance = self.acc.get_balance()

        # then
        self.assertEqual(balance, 0)

    def test_transfer(self):
        # when
        self.acc.transfer(-100)
        balance = self.acc.balance

        # then
        self.assertEqual(balance, -100)



    def test_transfer2(self):
        # when
        self.acc.transfer(-10)
        self.acc.transfer(50)
        balance = self.acc.balance

        # then
        self.assertEqual(balance, 40)

    def test_transfer2(self):
        # when
        self.acc.transfer(-100)
        self.acc.transfer(100)
        balance = self.acc.balance

        # then
        self.assertEqual(balance, 0)


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





