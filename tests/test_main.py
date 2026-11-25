import unittest
import main


class TestExpenseTracker(unittest.TestCase):

    def setUp(self):
        main.expenses.clear()

    def test_add_expense(self):
        expense = main.add_expense("Food", 150, "Food")
        self.assertEqual(expense["name"], "Food")
        self.assertEqual(expense["amount"], 150.0)

    def test_calculate_total(self):
        main.add_expense("Food", 150, "Food")
        main.add_expense("Travel", 50, "Travel")
        self.assertEqual(main.calculate_total(), 200)

    def test_category_total(self):
        main.add_expense("Food", 150, "Food")
        main.add_expense("Lunch", 100, "Food")
        main.add_expense("Bus", 50, "Travel")
        self.assertEqual(main.calculate_category_total("Food"), 250)

    def test_negative_amount(self):
        with self.assertRaises(ValueError):
            main.add_expense("Food", -100, "Food")

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            main.add_expense("", 100, "Food")

    def test_delete_expense(self):
        main.add_expense("Food", 150, "Food")
        deleted = main.delete_expense(0)
        self.assertEqual(deleted["name"], "Food")
        self.assertEqual(len(main.get_expenses()), 0)

    def test_invalid_delete_index(self):
        with self.assertRaises(IndexError):
            main.delete_expense(5)


if __name__ == "__main__":
    unittest.main()