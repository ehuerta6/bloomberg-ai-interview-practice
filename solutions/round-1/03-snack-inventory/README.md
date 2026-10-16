# Cappy's Snack Inventory Reference Solution

## What Was Wrong?

The starter allowed negative reservations, which increased stock. It also changed stock to zero when a reservation was too large. A misleading test expected a negative reservation to succeed.

## How to Find It

Inspect `restock` and `reserve` in `inventory.py`. Try a negative quantity and a reservation larger than the available stock, then check `quantities` after each call.

## The Fix

Both operations accept only positive integers, excluding booleans. A reservation checks availability before changing the quantity, so failed or invalid operations leave inventory unchanged and stock never becomes negative.

## Tests

The tests cover restocking, successful and exact reservations, insufficient stock, and invalid negative, zero, float, boolean, and string quantities. Failed operations assert the original quantity.

## How to Run

From this folder:

```sh
python3 inventory.py
```
