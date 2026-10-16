class OrderRepository:
    def __init__(self):
        self.orders = {}

    def get(self, order_id):
        return self.orders.get(order_id)

    def save(self, order):
        self.orders[order.order_id] = order
        return order
