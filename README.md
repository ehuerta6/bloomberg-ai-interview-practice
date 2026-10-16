# Coding Interview Club: Bloomberg AI Interview Practice

The Coding Interview Club created these five Python exercises to help students practice debugging with an AI helper. Their workflow draws on one club member's prep and mock-interview notes. The exercises are original practice, not actual or leaked Bloomberg questions or official interview requirements. Formats and tools can vary, so follow the instructions you receive.

## Challenge Portal

Open the [CIC Challenge Portal](https://ehuerta6.github.io/bloomberg-ai-interview-practice/) to choose a practice exercise and read its assignment in the browser. Then clone this repository, open only the selected exercise folder in VS Code, and run its command from that folder. Use a non-editing AI helper to investigate the code; make and explain the changes yourself.

GitHub Pages serves the portal from the repository settings: choose **Deploy from a branch**, set **Branch** to `main`, set **Folder** to `/docs`, and save.

## Get started

Clone the repository:

```sh
git clone https://github.com/ehuerta6/bloomberg-ai-interview-practice.git
cd bloomberg-ai-interview-practice
```

Choose an exercise below. Read its PR or Ticket in the Challenge Portal, then open only that exercise folder in VS Code with **File → Open Folder**. If the VS Code command-line tool is enabled, `code round-1/01-code-validator` opens the first exercise from the repository root. Keeping your editor focused on the selected exercise helps limit what your AI tool sees.

| ID | Exercise | Assignment | Open this folder | Run from that folder |
| --- | --- | --- | --- | --- |
| `r1-p1` | Student Code Validator | [`Code Validator assignment`](https://ehuerta6.github.io/bloomberg-ai-interview-practice/challenges/r1-01-code-validator.html) | `round-1/01-code-validator` | `python3 validator.py` |
| `r1-p2` | Event Scheduler | [`Event Scheduler assignment`](https://ehuerta6.github.io/bloomberg-ai-interview-practice/challenges/r1-02-event-scheduler.html) | `round-1/02-event-scheduler` | `python3 scheduler.py` |
| `r1-p3` | Cappy's Snack Inventory | [`Snack Inventory assignment`](https://ehuerta6.github.io/bloomberg-ai-interview-practice/challenges/r1-03-snack-inventory.html) | `round-1/03-snack-inventory` | `python3 inventory.py` |
| `r2-p1` | Cappy Event Registration System | [`Event Registration assignment`](https://ehuerta6.github.io/bloomberg-ai-interview-practice/challenges/r2-01-event-registration.html) | `round-2/01-event-registration` | `python3 test_event_registration.py` |
| `r2-p2` | Cappy Orders | [`Order Processing assignment`](https://ehuerta6.github.io/bloomberg-ai-interview-practice/challenges/r2-02-order-processing.html) | `round-2/02-order-processing` | `python3 test_order_processing.py` |

For example, from a terminal at the repository root, start Round 1, Problem 1 with:

```sh
cd round-1/01-code-validator
python3 validator.py
```

If you opened that problem folder directly in VS Code, its terminal is already there; run `python3 validator.py`. On some systems, use `python` instead. The exercises use Python's standard library, so no package installation or virtual environment is needed.

## Reference Solutions

The Bloomberg Interview Preparation Night workshop has concluded, so reference solutions are now publicly available. Use the original exercises to investigate the bugs first, then compare your work with the corrected implementation and explanation.

- [Round 1 · Code Validator](https://github.com/ehuerta6/bloomberg-ai-interview-practice/blob/main/solutions/round-1/01-code-validator/README.md)
- [Round 1 · Event Scheduler](https://github.com/ehuerta6/bloomberg-ai-interview-practice/blob/main/solutions/round-1/02-event-scheduler/README.md)
- [Round 1 · Cappy's Snack Inventory](https://github.com/ehuerta6/bloomberg-ai-interview-practice/blob/main/solutions/round-1/03-snack-inventory/README.md)
- [Round 2 · Event Registration](https://github.com/ehuerta6/bloomberg-ai-interview-practice/blob/main/solutions/round-2/01-event-registration/README.md)
- [Round 2 · Order Processing](https://github.com/ehuerta6/bloomberg-ai-interview-practice/blob/main/solutions/round-2/02-order-processing/README.md)

The `round-1/` and `round-2/` directories contain the original starter exercises, including their intentionally incomplete or misleading tests. The `solutions/` directory contains corrected implementations, tests, and explanations. These remain original CIC practice exercises, not official Bloomberg interview questions.

## What you'll practice

Round 1 is pull request review in a single Python file. The implementation and `unittest` tests are together in that file. Round 2 gives you a small multi-file codebase and an engineering ticket; trace how a request and its state move between modules.

Use this sequence: **Read the assignment. Inspect the code. Find a gap. Fix and test it.** Try a concrete input, check what the tests actually assert, and add a regression test for the behavior you investigate. Some starter tests are meant to fail. Others may be misleading, unrelated, or incomplete, so passing tests alone do not prove the code is right.

## Work with AI

Use AI to explain a function or traceback, trace a value through the code, or help think of a test. For example: “For this input, the code returns X. What should I inspect to understand why?” Ask it to point to evidence, then check that evidence yourself. Make the changes and explain your reasoning; the AI should help you investigate, not do the exercise for you.

The exercise's `AGENTS.md` asks the helper to read only that folder, avoid searching elsewhere for assignments or solutions, offer hints gradually, and leave all edits to you. These instructions guide behavior; they cannot restrict filesystem access, so an AI tool may still be able to read other folders. Open only the selected exercise in your editor and choose a read-only or non-editing AI mode; keep edit or agent mode off. Check the tool's access, and share the relevant assignment details yourself when you want help reasoning about them.

## Resources

- [Python `unittest`](https://docs.python.org/3/library/unittest.html)
- [HackerRank: AI Assistant in Interviews](https://candidatesupport.hackerrank.com/articles/6665907643-ai-assistant-in-interviews)
- [GitHub Copilot prompt engineering](https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering)
- [GitHub Copilot: Explore a codebase](https://docs.github.com/en/copilot/tutorials/explore-a-codebase)
- [Martin Fowler: Test-Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html)

Corrected solutions and explanations are kept on a separate local branch for workshop staff. They will be published after the workshop, with authorization. Cappy, the club's capybara, appears in a few exercise names.
