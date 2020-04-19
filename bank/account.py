from faker import Faker

from bank.card import Card


class Account:
    def __init__(self, name, surname):
        fake = Faker()
        self.number = fake.iban()
        self.owner = name + " " + surname
        self.balance = 0

    def create_new_card(self, pin):
        return Card(self, pin)

    def __str__(self):
        return self.number

    def transfer(self, money):
        self.balance += money

