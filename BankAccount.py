from unittest import TestCase
import unittest

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Bank account: {self.owner}, balance: {self.balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("you can not add this sum of money")

    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
            if self.balance < 0:
                raise ValueError("you do not have enough money for this operation")
        else:
            raise ValueError("you can not add this sum of money")

    def get_balance(self):
        return self.balance




class BankAccountTest(TestCase):
    def test_create_account(self):
        owner = "Valery"
        balance = 1000
        result = BankAccount(owner, balance)
        self.assertEqual(result.owner, owner)
        self.assertEqual(result.balance, balance)

    def test_deposit_amount(self):
        accaunt = BankAccount("Valery", 1000)
        accaunt.deposit(100)
        self.assertEqual(accaunt.balance, 1100)

    def test_deposit_with_negative(self):
        accaunt = BankAccount("Valery", 1000)
        with self.assertRaises(ValueError):
            accaunt.deposit(-100)


    def test_withdraw_amount(self):
        accaunt = BankAccount("Valery", 1000)
        accaunt.withdraw(100)
        self.assertEqual(accaunt.balance, 900)

    def test_withdraw_too_much(self):
        accaunt = BankAccount("Valery", 1000)
        with self.assertRaises(ValueError):
            accaunt.withdraw(1100)


if __name__ == "__main__":
    unittest.main()






