# Event Registration Reference Solution

## What Was Wrong?

The service counted every registration when checking capacity. Cancellation kept the record for history but changed its status to `cancelled`, so the cancelled record still incorrectly filled a seat.

## How to Find It

Trace a request through `registration_routes.py`, `registration_service.py`, and `event_repository.py`. Fill the event, cancel one registration, then try registering another student. Inspect the status filter used by the capacity check.

## The Fix

Capacity counts only registrations whose status is `active`. The existing active-registration lookup prevents duplicate active registrations. Cancellation changes an active record once; missing or already-cancelled records are rejected without changing state.

## Tests

The tests fill capacity, reject an additional registration, cancel a registration and replace it, reject duplicate active registrations, allow a cancelled student to register again, and reject repeated or invalid cancellation requests. They assert real status codes and repository state.

## How to Run

From this folder:

```sh
python3 test_event_registration.py
```
