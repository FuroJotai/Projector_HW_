import unittest
from Bank_script import Bank, SavingsAccount, CurrentAccount
from unittest.mock import patch


class TestBank(unittest.TestCase):

    def test_is_open(self):
        
        bank = Bank()

        savings_acc = SavingsAccount(1, 1000, 0.5)

        bank.open_account(savings_acc)
        self.assertIn(1, bank.accounts)
        
        account1 = bank.accounts[1]
        self.assertEqual(account1.balance, 1000)
        self.assertEqual(account1.interest_rate, 0.5)
        self.assertIsInstance(account1, SavingsAccount)

    def test_update_accounts(self):
        bank = Bank()
        
        savings_acc1 = SavingsAccount(1, 1000, 0.5)
        savings_acc2 = SavingsAccount(2, 2000, 0.3)
        bank.open_account(savings_acc1)
        bank.open_account(savings_acc2)
        
        current_acc = CurrentAccount(3, -200, 100)
        bank.open_account(current_acc)

        current_acc.balance=-250
        
        bank.update_accounts()

        self.assertEqual(savings_acc1.balance, 1005)
        self.assertEqual(savings_acc2.balance, 2006)

        with patch('builtins.print') as mocked_print:
            bank.update_accounts()
            mocked_print.assert_called_once_with("Overdraft letter sent for Account 3")

if __name__ == '__main__':
    unittest.main()