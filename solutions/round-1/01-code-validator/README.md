# Code Validator Reference Solution

## What Was Wrong?

The starter converted the code to an integer before checking its length. That removed leading zeroes, so a valid code such as `001234` failed. Numeric parsing also accepts digit characters that are not ASCII, and the original arithmetic assertion did not test the validator.

## How to Find It

Inspect `is_valid_access_code` in `validator.py`. Try `001234`, a full-width digit string, and an integer. The results expose the difference between preserving the input string and converting it first.

## The Fix

The function first requires a string, then checks for exactly six characters. It compares each character with the ASCII range `0` through `9`, so leading zeroes stay intact and other Unicode digits are rejected.

## Tests

The tests cover valid codes, leading zeroes, wrong lengths, letters, spaces, non-ASCII digits, and non-string values. Invalid inputs return `False` without raising.

## How to Run

From this folder:

```sh
python3 validator.py
```
