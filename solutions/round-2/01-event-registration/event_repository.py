from event_models import Event, Registration


class EventRepository:
    def __init__(self):
        self.events = {}
        self.registrations = {}

    def add_event(self, event):
        self.events[event.event_id] = event

    def get_event(self, event_id):
        return self.events.get(event_id)

    def save_registration(self, registration):
        self.registrations[registration.registration_id] = registration
        return registration

    def for_event(self, event_id):
        return [r for r in self.registrations.values() if r.event_id == event_id]

    def active_for_student(self, event_id, student_id):
        return [
            r for r in self.for_event(event_id)
            if r.student_id == student_id and r.status == "active"
        ]

    def get_registration(self, registration_id):
        return self.registrations.get(registration_id)
