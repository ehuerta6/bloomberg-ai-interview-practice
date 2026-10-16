class RegistrationRoutes:
    """Small route adapter used to keep request handling separate from rules."""

    def __init__(self, service):
        self.service = service

    def post_registration(self, payload):
        required = ("event_id", "student_id", "registration_id")
        if any(not payload.get(field) for field in required):
            return {"status": 400}
        created = self.service.register(
            payload["event_id"], payload["student_id"], payload["registration_id"]
        )
        return {"status": 201 if created else 409}

    def delete_registration(self, registration_id):
        return {"status": 200 if self.service.cancel(registration_id) else 404}
