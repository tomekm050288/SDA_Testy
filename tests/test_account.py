import unittest
from faker import Faker
from bank.account import Account


class AccountTest(unittest.TestCase):
    def setUp(self):
        Faker.seed(0)
        self.acc = Account("John", "Doe")

    def test_basic(self):
        acc_number = str(self.acc)
        self.assertEquals(acc_number, 'GB22VTKG87647593824219')

    def test_basic_2(self):
        Faker.seed(1)
        acc_number = str(Account("John", "Doe"))

        self.assertEquals(acc_number, 'GB42DWTG77763170669074')

    def test_owner(self):
        # when
        owner = self.acc.owner

        # then
        self.assertEquals(owner, "John Doe")

    def test_balance(self):
        # when
        balance = self.acc.balance

        # then
        self.assertEquals(balance, 0)

    def test_number(self):
        # when
        number = self.acc.number

        # then
        self.assertEquals(number, 'GB22VTKG87647593824219')

    def test_transfer(self):
        # when
        self.acc.transfer(-50)
        balance = self.acc.balance

        # then
        self.assertEquals(balance, -50)

    def test_transfer2(self):
        # when
        self.acc.transfer(-50)
        self.acc.transfer(-50)
        balance = self.acc.balance

        # then
        self.assertEquals(balance, -100)

    def test_transfer3(self):
        # when
        self.acc.transfer(50)
        self.acc.transfer(-50)
        balance = self.acc.balance

        # then
        self.assertEquals(balance, 0)


