import unittest

from event_models import Event
from event_repository import EventRepository
from registration_routes import RegistrationRoutes
from registration_service import RegistrationService


class RegistrationTests(unittest.TestCase):
    def setUp(self):
        self.repo = EventRepository()
        self.repo.add_event(Event("career-night", 2))
        self.registration_routes = RegistrationRoutes(RegistrationService(self.repo))

    def register(self, student, registration):
        return self.registration_routes.post_registration({
            "event_id": "career-night",
            "student_id": student,
            "registration_id": registration,
        })

    def test_capacity_counts_only_active_registrations(self):
        self.assertEqual(self.register("s1", "r1")["status"], 201)
        self.assertEqual(self.register("s2", "r2")["status"], 201)
        self.assertEqual(self.register("s3", "r3")["status"], 409)

    def test_cancelled_registration_frees_capacity(self):
        self.register("s1", "r1")
        self.register("s2", "r2")
        self.assertEqual(self.registration_routes.delete_registration("r1")["status"], 200)
        self.assertEqual(self.register("s3", "r3")["status"], 201)

    def test_duplicate_active_registration_is_rejected(self):
        self.register("s1", "r1")
        self.assertEqual(self.register("s1", "r2")["status"], 409)

    def test_registration_id_cannot_replace_existing_registration(self):
        self.assertEqual(self.register("s1", "r1")["status"], 201)
        self.assertEqual(self.register("s2", "r1")["status"], 409)
        self.assertEqual(self.repo.get_registration("r1").student_id, "s1")
        self.assertEqual(self.repo.get_registration("r1").status, "active")

    def test_cancelled_student_can_register_again(self):
        self.register("s1", "r1")
        self.assertEqual(self.registration_routes.delete_registration("r1")["status"], 200)
        self.assertEqual(self.register("s1", "r2")["status"], 201)

    def test_cancel_is_rejected_after_first_cancel(self):
        self.register("s1", "r1")
        self.assertEqual(self.registration_routes.delete_registration("r1")["status"], 200)
        self.assertEqual(self.registration_routes.delete_registration("r1")["status"], 404)
        self.assertEqual(self.repo.get_registration("r1").status, "cancelled")

    def test_unknown_cancellation_is_rejected_without_changing_state(self):
        self.register("s1", "r1")
        self.assertEqual(self.registration_routes.delete_registration("missing")["status"], 404)
        self.assertEqual(self.repo.get_registration("r1").status, "active")

    def test_unknown_event_and_missing_fields_are_rejected(self):
        response = self.registration_routes.post_registration({
            "event_id": "missing",
            "student_id": "s",
            "registration_id": "r",
        })
        self.assertEqual(response["status"], 409)
        self.assertEqual(self.registration_routes.post_registration({"event_id": "career-night"})["status"], 400)


if __name__ == "__main__":
    unittest.main()
