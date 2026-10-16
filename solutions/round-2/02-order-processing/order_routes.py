class OrderRoutes:
    def __init__(self, orders):
        self.orders = orders

    def submit(self, payload):
        required = ("order_id", "student_id", "item", "quantity")
        if any(key not in payload for key in required):
            return {"status": 400}
        order = self.orders.place_order(
            payload["order_id"],
            payload["student_id"],
            payload["item"],
            payload["quantity"],
        )
        return {"status": 201 if order else 409}
