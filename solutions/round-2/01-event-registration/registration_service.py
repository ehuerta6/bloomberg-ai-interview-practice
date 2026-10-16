from event_models import Registration


class RegistrationService:
    def __init__(self, event_repository):
        self.event_repository = event_repository

    def register(self, event_id, student_id, registration_id):
        event = self.event_repository.get_event(event_id)
        if event is None or not event_id or not student_id or not registration_id:
            return False
        if self.event_repository.get_registration(registration_id) is not None:
            return False
        active = [
            registration
            for registration in self.event_repository.for_event(event_id)
            if registration.status == "active"
        ]
        if len(active) >= event.capacity:
            return False
        if self.event_repository.active_for_student(event_id, student_id):
            return False
        self.event_repository.save_registration(
            Registration(registration_id, event_id, student_id)
        )
        return True

    def cancel(self, registration_id):
        registration = self.event_repository.get_registration(registration_id)
        if registration is None or registration.status != "active":
            return False
        registration.status = "cancelled"
        return True
