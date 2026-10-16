import unittest


class SnackInventory:
    def __init__(self, quantities=None):
        self.quantities = dict(quantities or {})

    @staticmethod
    def _is_valid_quantity(quantity):
        return isinstance(quantity, int) and not isinstance(quantity, bool) and quantity > 0

    def restock(self, snack, quantity):
        if not self._is_valid_quantity(quantity):
            return False
        self.quantities[snack] = self.quantities.get(snack, 0) + quantity
        return True

    def reserve(self, snack, quantity):
        if not self._is_valid_quantity(quantity):
            return False
        available = self.quantities.get(snack, 0)
        if available < quantity:
            return False
        self.quantities[snack] = available - quantity
        return True


class InventoryTests(unittest.TestCase):
    def test_restock_increases_quantity(self):
        stock = SnackInventory({"apples": 2})
        self.assertTrue(stock.restock("apples", 3))
        self.assertEqual(stock.quantities["apples"], 5)

    def test_successful_reservation_reduces_quantity(self):
        stock = SnackInventory({"bars": 4})
        self.assertTrue(stock.reserve("bars", 2))
        self.assertEqual(stock.quantities["bars"], 2)

    def test_failed_reservation_preserves_stock(self):
        stock = SnackInventory({"bars": 2})
        self.assertFalse(stock.reserve("bars", 5))
        self.assertEqual(stock.quantities["bars"], 2)

    def test_invalid_restock_quantities_do_not_change_stock(self):
        for quantity in (-1, 0, 1.5, True, "2"):
            with self.subTest(quantity=quantity):
                stock = SnackInventory({"bars": 2})
                self.assertFalse(stock.restock("bars", quantity))
                self.assertEqual(stock.quantities["bars"], 2)

    def test_invalid_reservation_quantities_do_not_change_stock(self):
        for quantity in (-1, 0, 1.5, True, "2"):
            with self.subTest(quantity=quantity):
                stock = SnackInventory({"bars": 2})
                self.assertFalse(stock.reserve("bars", quantity))
                self.assertEqual(stock.quantities["bars"], 2)

    def test_reserving_exact_available_quantity_leaves_zero(self):
        stock = SnackInventory({"bars": 2})
        self.assertTrue(stock.reserve("bars", 2))
        self.assertEqual(stock.quantities["bars"], 0)


if __name__ == "__main__":
    unittest.main()
