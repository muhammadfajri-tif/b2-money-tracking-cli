import unittest
import sys

sys.path.append("src/")
from core.transaction import Transaction, TransactionType


class TestTransaction(unittest.TestCase):

    def test_transaction_creation(self):
        # Test creating a transaction object
        transaction = Transaction(
            TransactionType.INCOME, "2024-03-22", 100, "Salary", "Monthly income"
        )

        self.assertEqual(transaction.type, TransactionType.INCOME)
        self.assertEqual(transaction.date, "2024-03-22")
        self.assertEqual(transaction.amount, 100)
        self.assertEqual(transaction.category, "Salary")
        self.assertEqual(transaction.desc, "Monthly income")

    def test_validate_transaction_type(self):
        # Test validating transaction types
        self.assertTrue(Transaction.validate_transaction_type(TransactionType.INCOME))
        self.assertTrue(Transaction.validate_transaction_type(TransactionType.SPENDING))
        self.assertFalse(Transaction.validate_transaction_type("InvalidType"))

    def test_repr_method(self):
        # Test __repr__ method
        transaction = Transaction(
            TransactionType.INCOME, "2024-03-22", 100, "Salary", "Monthly income"
        )
        expected_repr = "{\n\tType: income\n\tDate: 2024-03-22\n\tAmount: 100\n\tCategory: Salary\n\tDesc: Monthly income\n}\n"
        self.assertEqual(repr(transaction), expected_repr)


if __name__ == "__main__":
    unittest.main()
