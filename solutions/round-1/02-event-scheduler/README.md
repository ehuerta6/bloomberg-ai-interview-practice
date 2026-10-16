# Event Scheduler Reference Solution

## What Was Wrong?

The starter treated events touching at a boundary as conflicts and added a checked event to the input list. It also allowed empty intervals. Those behaviors contradict the half-open interval and read-only requirements.

## How to Find It

Inspect `is_available` in `scheduler.py`. Compare an existing event `(10, 12)` with candidates starting at `12` or ending at `10`, then inspect the list after the call. Try `(5, 5)` as well.

## The Fix

The function rejects `start >= end`. For valid intervals it uses the half-open overlap condition `start < event_end and event_start < end`. It only reads `events`; booking a confirmed event remains the caller's responsibility.

## Tests

The tests cover overlap, both adjacent boundaries, disjoint events, empty and reversed intervals, and list contents after both available and conflicting checks.

## How to Run

From this folder:

```sh
python3 scheduler.py
```
