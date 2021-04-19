class BankAccount:

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
    @property
    def provrka (self):
        if self._name == 'den':
            return 'den'
        return 'error'
    @property
    def hz (self):
        if self._balance <= 0:
            return "fuse box"
        return self._balance



account = BankAccount('den', 90)
account._balance = 999999999999999
account._name = 'den'
# Cчет пользователя {self._balance}
print(account.hz, 'hacker')
print(account.provrka)
