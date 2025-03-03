# bank_account.py

import unittest

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Deposit amount must be positive')
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Withdrawal amount must be positive')
        if amount > self.balance:
            raise ValueError('Insufficient funds')
        self.balance -= amount


# Test case class for BankAccount
class TestBankAccount(unittest.TestCase):

    # Setup method: Create a BankAccount instance with an initial balance of 100
    def setUp(self):
        self.account = BankAccount(100)

    # Teardown method: Clean up resources after each test
    def tearDown(self):
        self.account = None

    # Test the initial balance
    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 100)  # Verify the initial balance is set to 100

    # Test deposit of a positive amount
    def test_deposit_positive_amount(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)  # Verify the new balance is 150 after depositing 50

    # Test deposit of zero amount (should raise ValueError)
    def test_deposit_zero_amount(self):
        with self.assertRaises(ValueError):  # Deposit 0 should raise an error
            self.account.deposit(0)

    # Test deposit of a negative amount (should raise ValueError)
    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):  # Deposit of negative value should raise an error
            self.account.deposit(-20)

    # Test withdrawal of a positive amount
    def test_withdraw_positive_amount(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.balance, 70)  # Verify the new balance is 70 after withdrawing 30

    # Test withdrawal of more than available balance (should raise ValueError)
    def test_withdraw_more_than_balance(self):
        with self.assertRaises(ValueError):  # Withdrawal more than available should raise an error
            self.account.withdraw(200)

    # Test withdrawal of zero amount (should raise ValueError)
    def test_withdraw_zero_amount(self):
        with self.assertRaises(ValueError):  # Withdrawal 0 should raise an error
            self.account.withdraw(0)

    # Test withdrawal of a negative amount (should raise ValueError)
    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):  # Withdrawal of negative amount should raise an error
            self.account.withdraw(-20)

if __name__ == '__main__':
    unittest.main()
