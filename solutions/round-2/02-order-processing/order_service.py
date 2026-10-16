from order_models import Order


class OrderService:
    def __init__(self, inventory, payment_service, order_repository):
        self.inventory = inventory
        self.payment_service = payment_service
        self.order_repository = order_repository

    def place_order(self, order_id, student_id, item, quantity):
        if not all(isinstance(value, str) and value for value in (order_id, student_id, item)):
            return None
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
            return None
        existing = self.order_repository.get(order_id)
        if existing and existing.status == "completed":
            return existing
        if not self.inventory.reserve(order_id, item, quantity):
            return None
        order = Order(order_id, student_id, item, quantity)
        self.order_repository.save(order)
        if not self.payment_service.authorize(order_id, student_id):
            order.status = "failed"
            self.inventory.release(order_id)
            return None
        self.inventory.commit(order_id)
        order.status = "completed"
        return order
