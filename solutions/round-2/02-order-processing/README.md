# Order Processing Reference Solution

## What Was Wrong?

The starter deducted inventory before payment and did not reliably undo that deduction when authorization failed. A failed order could therefore make stock disappear. The flow also needed to prevent a completed order retry from applying its effects again.

## How to Find It

Trace one request through `order_routes.py`, `order_service.py`, `inventory.py`, and `payment_service.py`. Use a payment service configured to reject the order, then inspect both `quantities` and `reservations`. Submit the same successful order identifier twice and compare payment calls and stock.

## The Fix

The service validates the request, reserves stock, and saves the pending order before authorization. A failed authorization marks the order failed and releases the reservation. A successful authorization commits the reservation, and a completed order is returned immediately on retry without another deduction or payment call.

## Tests

The tests assert inventory quantities and reservations for successful orders, failed payments, invalid orders, and insufficient stock. They also verify that completed retries are idempotent and that a failed order can be retried after payment approval recovers.

## How to Run

From this folder:

```sh
python3 test_order_processing.py
```
