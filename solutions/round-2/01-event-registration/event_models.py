from dataclasses import dataclass


@dataclass
class Event:
    event_id: str
    capacity: int


@dataclass
class Registration:
    registration_id: str
    event_id: str
    student_id: str
    status: str = "active"
