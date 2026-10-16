class FakePaymentService:
    def __init__(self, approved=True):
        self.approved = approved
        self.authorizations = []

    def authorize(self, order_id, student_id):
        self.authorizations.append(order_id)
        return self.approved
