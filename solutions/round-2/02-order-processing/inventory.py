class Inventory:
    def __init__(self, quantities=None):
        self.quantities = dict(quantities or {})
        self.reservations = {}

    def reserve(self, order_id, item, quantity):
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
            return False
        if order_id in self.reservations:
            return False
        available = self.quantities.get(item, 0)
        if available < quantity:
            return False
        self.quantities[item] = available - quantity
        self.reservations[order_id] = (item, quantity)
        return True

    def release(self, order_id):
        reservation = self.reservations.pop(order_id, None)
        if reservation is None:
            return False
        item, quantity = reservation
        self.quantities[item] = self.quantities.get(item, 0) + quantity
        return True

    def commit(self, order_id):
        """Finalize an already deducted reservation after payment succeeds."""
        return self.reservations.pop(order_id, None) is not None
