"""
Создайте класс BankAccount, который представляет банковский счет, c атрибутами экземпляра:
accountNumber (числовой тип), name (имя владельца счета строкового типа), balance.
Создайте конструктор с параметрами: accountNumber, name, balance.
Создайте метод Deposit(), который управляет действиями по пополнению счета.
Создайте метод Withdrawal(), который управляет действиями по снятию средств.
Создайте метод bankFees() для применения банковской комиссии в размере 5% от баланса счета.
Создайте метод display() для отображения деталей счета.
Приведите примеры использования.
"""

# class BankAccount:
#
#
#     def __init__(self, acc_number, name):
#         self.acc_number = acc_number
#         self.name = name
#         self.balance = 0
#         self._status = None
#
#     @property
#     def status(self):
#         return self._status
#
#     @status.setter
#     def status(self, status):
#         if status == 0:
#             self._status = False
#         else:
#             self._status = True


#     def deposit(self):
#         my_amount = float(input("Enter amount to be deposited: "))
#         self.balance += my_amount
#         return f"My Balance is: ", self.balance
#
#     def bank_fees(self, amount):
#         return amount * 0.05
#
#     def withdrawal(self):
#         w_amount = float(input("Enter amount to be withdrown: "))
#         if self.balance >= w_amount:
#             self.balance -= w_amount + self.bank_fees(w_amount)
#             print(self.balance)
#
#         else:
#             print("Low balance")
#
#
#
#
#
# bank = BankAccount(12345678, "Nazir")
# bank.status = None
# print(bank.status)
# # print(bank.deposit())
# bank.withdrawal()


class BankAccount:

    def __init__(self, account_number, name):
        self.account_number = account_number
        self.name = name
        self.balance = 0
        self._status = None

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if status == 0:
            self._status = False
        else:
            self._status = True

    # @status.deleter

    def deposit(self, money):
        """
        метод управляет действиями по пополнению счета.
        """
        self.balance += money
        return f'Now, your balance is ${self.balance}.'

    @staticmethod
    def __bank_fees(money):
        """
        метод для применения банковской комиссии в размере 5% от суммы снятия.
        """
        return money * 0.05

    def withdrawal(self, money):
        """
        метод управляет действиями по снятию средств.
        """
        self.balance -= money + self.__bank_fees(money)
        return f''

    def display(self):
        """
        метод для отображения деталей счета.
        """
        return 'bla bla bla'


card1 = BankAccount(213124, 'kfc')
card1.status = None
print(card1.status)





