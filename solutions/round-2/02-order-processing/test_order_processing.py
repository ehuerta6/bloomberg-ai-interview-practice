import unittest

from inventory import Inventory
from order_routes import OrderRoutes
from order_service import OrderService
from payment_service import FakePaymentService
from order_repository import OrderRepository


class OrderTests(unittest.TestCase):
    def build(self, approved=True):
        inventory = Inventory({"club-shirt": 5})
        payment_service = FakePaymentService(approved)
        order_repository = OrderRepository()
        service = OrderService(inventory, payment_service, order_repository)
        return inventory, payment_service, order_repository, OrderRoutes(service)

    def payload(self, order_id="o1", quantity=2):
        return {
            "order_id": order_id,
            "student_id": "s1",
            "item": "club-shirt",
            "quantity": quantity,
        }

    def test_successful_order_deducts_once_and_commits_reservation(self):
        inventory, payment_service, order_repository, routes = self.build()
        self.assertEqual(routes.submit(self.payload())["status"], 201)
        self.assertEqual(inventory.quantities["club-shirt"], 3)
        self.assertEqual(inventory.reservations, {})
        self.assertEqual(order_repository.get("o1").status, "completed")

    def test_failed_payment_releases_reservation_and_preserves_inventory(self):
        inventory, payment_service, order_repository, routes = self.build(approved=False)
        self.assertEqual(routes.submit(self.payload())["status"], 409)
        self.assertEqual(inventory.quantities["club-shirt"], 5)
        self.assertEqual(inventory.reservations, {})
        self.assertEqual(order_repository.get("o1").status, "failed")

    def test_retry_of_completed_order_has_no_duplicate_effects(self):
        inventory, payment_service, _, routes = self.build()
        self.assertEqual(routes.submit(self.payload())["status"], 201)
        self.assertEqual(routes.submit(self.payload())["status"], 201)
        self.assertEqual(inventory.quantities["club-shirt"], 3)
        self.assertEqual(len(payment_service.authorizations), 1)

    def test_unhashable_order_id_is_rejected_without_state_change(self):
        inventory, payment_service, _, routes = self.build()
        self.assertEqual(routes.submit(self.payload(order_id=[]))["status"], 409)
        self.assertEqual(inventory.quantities["club-shirt"], 5)
        self.assertEqual(inventory.reservations, {})
        self.assertEqual(payment_service.authorizations, [])

    def test_invalid_completed_order_retry_is_rejected(self):
        inventory, payment_service, _, routes = self.build()
        self.assertEqual(routes.submit(self.payload())["status"], 201)
        invalid_retry = {
            "order_id": "o1",
            "student_id": "",
            "item": "club-shirt",
            "quantity": -2,
        }
        self.assertEqual(routes.submit(invalid_retry)["status"], 409)
        self.assertEqual(inventory.quantities["club-shirt"], 3)
        self.assertEqual(inventory.reservations, {})
        self.assertEqual(len(payment_service.authorizations), 1)

    def test_invalid_orders_do_not_change_inventory_or_payment_state(self):
        inventory, payment_service, _, routes = self.build()
        for quantity in (0, -1, 1.5, True, "2"):
            with self.subTest(quantity=quantity):
                self.assertEqual(routes.submit(self.payload(order_id=f"bad-{quantity}", quantity=quantity))["status"], 409)
        self.assertEqual(routes.submit({"order_id": "missing"})["status"], 400)
        self.assertEqual(inventory.quantities["club-shirt"], 5)
        self.assertEqual(inventory.reservations, {})
        self.assertEqual(payment_service.authorizations, [])

    def test_insufficient_stock_fails_without_payment_or_partial_deduction(self):
        inventory, payment_service, _, routes = self.build()
        self.assertEqual(routes.submit(self.payload(quantity=6))["status"], 409)
        self.assertEqual(inventory.quantities["club-shirt"], 5)
        self.assertEqual(payment_service.authorizations, [])

    def test_failed_order_can_be_retried_after_authorization_recovers(self):
        inventory = Inventory({"club-shirt": 5})
        payment_service = FakePaymentService(approved=False)
        order_repository = OrderRepository()
        service = OrderService(inventory, payment_service, order_repository)
        first = service.place_order("o1", "s1", "club-shirt", 2)
        self.assertIsNone(first)
        payment_service.approved = True
        second = service.place_order("o1", "s1", "club-shirt", 2)
        self.assertEqual(second.status, "completed")
        self.assertEqual(inventory.quantities["club-shirt"], 3)
        self.assertEqual(inventory.reservations, {})


if __name__ == "__main__":
    unittest.main()
