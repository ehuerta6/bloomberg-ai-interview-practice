import unittest


def is_available(events, start, end):
    """Return whether [start, end) is valid and does not overlap an event."""
    if start >= end:
        return False
    return not any(
        start < event_end and event_start < end
        for event_start, event_end in events
    )


class SchedulerTests(unittest.TestCase):
    def test_overlapping_event_is_rejected(self):
        self.assertFalse(is_available([(10, 12)], 11, 13))

    def test_events_touching_at_either_boundary_are_allowed(self):
        self.assertTrue(is_available([(10, 12)], 12, 14))
        self.assertTrue(is_available([(10, 12)], 8, 10))

    def test_disjoint_event_is_allowed(self):
        self.assertTrue(is_available([(10, 12)], 13, 15))

    def test_empty_or_reversed_interval_is_rejected(self):
        self.assertFalse(is_available([], 5, 5))
        self.assertFalse(is_available([], 6, 5))

    def test_check_never_mutates_existing_events(self):
        events = [(10, 12)]
        self.assertTrue(is_available(events, 13, 15))
        self.assertEqual(events, [(10, 12)])
        self.assertFalse(is_available(events, 11, 13))
        self.assertEqual(events, [(10, 12)])


if __name__ == "__main__":
    unittest.main()
