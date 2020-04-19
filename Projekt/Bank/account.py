from faker import Faker
from Bank.card import Card

class Account:

    def __init__(self, name, surname):
        faker = Faker()
        self.acc_number = faker.iban()
        self.name = name
        self.surname = surname
        self.balance = 0

    def owner(self):
        return self.name + " " + self.surname

    def get_balance(self):
        return self.balance

    def transfer(self, amount):
        self.balance += amount

    def __str__(self):
        return self.acc_number

    def create_card(self, pin):
       return Card(self, pin)





