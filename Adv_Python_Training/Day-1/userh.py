class NotEnoughBalance(Exception):
    pass


class BankAccount:

    def __init__(self, initAmount):
        self.amount = initAmount

    def __str__(self):
        return (f"BankAccount amount is {self.amount}")

    def transaction(self, amount):
        if self.amount + amount < 0:
            raise NotEnoughBalance("Not Possible")
        self.amount = self.amount + amount


from abc import ABCMeta, abstractmethod


class BankUser(metaclass=ABCMeta):
    how_many_users = {'TotalUsers': 0}  # class variable, BankUser.how_many_users

    def __init__(self, name, initAmount):
        self.name = name  ## Instance Variable
        self.account = BankAccount(initAmount)
        self.update_user_types()

    @property  ## getter property
    def balance(self):
        return self.account.amount

    @balance.setter  ## Setter Method
    def balance(self, amount):
        raise NotImplementedError("Setting can only be done via transact method")

    def __str__(self):
        return f"{self.getUserType()} {self.name} , {self.balance}"

    @abstractmethod
    def getUserType(self):
        raise NotImplementedError("Not Implemented")

    @classmethod
    def howMany(cls):  ## BankUser.howMany()
        return cls.how_many_users

    def update_user_types(self):
        t = self.getUserType()
        if t in BankUser.how_many_users:
            BankUser.how_many_users[t] += 1
        else:
            BankUser.how_many_users[t] = 1
            BankUser.how_many_users['TotalUsers'] += 1

    @abstractmethod
    def getCashbackPercentage(self):
        return 0

    def transact(self, amount):
        try:
            self.account.transaction(amount)
            if amount < 0:
                cashback = self.getCashbackPercentage() * abs(amount)
                self.account.transaction(cashback)
        except NotEnoughBalance as ex:
            print(str(ex), " , Name : ", self.name, " , Amount : ", amount)


class NormalUser(BankUser):
    def getCashbackPercentage(self):
        return super().getCashbackPercentage()

    def getUserType(self):
        return "NormalUser"


class SilverUser(BankUser):
    def getCashbackPercentage(self):
        return 0.03

    def getUserType(self):
        return "SilverUser"


class GoldUser(BankUser):
    def getCashbackPercentage(self):
        return 0.05

    def getUserType(self):
        return "GoldUser"


if __name__ == '__main__':  # pragma: no cover
    users = [GoldUser("Gold", 100),
             SilverUser("Silver", 100),
             NormalUser("Normal", 100)]
    amounts = [100, -200, 300, -400, 400]
    for u in users:
        for am in amounts:
            u.transact(am)
        print(u, " , balance is :"  , u.balance)