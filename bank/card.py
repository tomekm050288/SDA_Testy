class Card:
    def __init__(self, acc, pin):
        self.acc = acc
        self.pin = pin

    @property
    def owner(self):
        return self.acc.owner

    def check_pin(self, pin):
        return self.pin == pin

    def is_pin_number(self):
        int(self.pin)
        return True

    def get_account(self):
        return self.acc