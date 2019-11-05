class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)

        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """The bank"""

    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def transfer(self, origin, dest, amount):
        """
            @origin: int(id) or str(name) of the first account
            @dest:    int(id) or str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return         True if success, False if an error occured
        """

        def checkaccount(self, acc):
            if type(acc) is int:
                acc = next((a for a in self.account if a.id == acc), None)
            elif type(acc) is str:
                acc = next((a for a in self.account if a.name == acc), None)

            if type(acc) is not Account:
                return False

            attrs = dir(acc)
            if len(attrs) % 2 == 0:
                return False
            if any(a for a in attrs if a.startswith('b')):
                return False
            if not any(a for a in attrs
                    if a.startswith('zip') or a.startswith('addr')):
                return False
            if 'name' not in attrs or \
                    'id' not in attrs or 'value' not in attrs:
                return False

        origin = checkaccount(self, origin)
        dest = checkaccount(self, dest)
        if not origin or not dest:
            return False

        if amount < 0 or amount > origin.value:
            return False

        origin.transfer(-amount)
        dest.transfer(amount)

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return         True if success, False if an error occured
        """

        if type(account) is int:
            account = next((a for a in self.account
                    if a.id == account), None)
        elif type(account) is str:
            account = next((a for a in self.account
                    if a.name == account), None)

        attrs = dir(account)

        if 'name' not in attrs:
            account.name = 'unicorn'
        if 'id' not in attrs:
            account.id = Account.ID_COUNT
            Account.ID_COUNT += 1
        if 'value' not in attrs:
            account.value = 0

        for att in attrs:
            if att.startswith('b'):
                del account[att]

        if not any(a for a in attrs
                if a.startswith('zip') or a.startswith('addr')):
            account.zip_unicorn = True

        attrs = dir(account)
        if len(attrs) % 2 == 0:
            att = 'unicorn'
            while att in account:
                att += '-'
            account[att] = True

