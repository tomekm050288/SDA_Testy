class Card:

    def __init__(self, account, pin):
        self.account = account
        self.pin = pin

    @property
    def card_owner(self):
        return self.account.owner()

    def check_pin(self, pin):
        return pin == self.pin

    def get_account(self):
        return str(self.account)

    def is_pin_number(self):
        int(self.pin)
        return True