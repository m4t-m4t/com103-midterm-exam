# com103-midterm-exam

# Dorm Room Chore Tracker

A beginner-friendly Python program that manages and tracks shared responsibilities in a dorm room setup.

---

## Overview

This project simulates a real-life scenario where four BSIT students share a dorm room and need a fair system to assign and monitor chores. The program allows a designated room monitor to assign tasks, track completion, and evaluate overall performance for the week.

It demonstrates the practical application of basic programming concepts in solving everyday problems.

---

## Features

* Displays a predefined list of dorm chores with their frequency
* Accepts up to 4 chore assignments
* Allows skipping a chore slot
* Tracks total assigned and completed chores
* Calculates completion rate (whole-number percentage)
* Generates a formatted weekly report
* Assigns a room status:

  * ROOM IS SPOTLESS! (100%)
  * ALMOST THERE! (50%–99%)
  * NEEDS CATCHING UP! (below 50%)

---

## Input Validation

The program enforces the following rules:

* Room Monitor Name: letters and spaces only
* Room Number: no spaces; only letters, numbers, dash (-), and underscore (_) allowed
* Chore Number: must be between 0–5 (0 means skip)
* Roommate Name: letters and spaces only
* Status: must be "done" or "not done"

---

## Chore List

| # | Chore              | Frequency       |
| - | ------------------ | --------------- |
| 1 | Sweeping / Mopping | Daily           |
| 2 | Dishwashing        | After meals     |
| 3 | Taking Out Trash   | Every other day |
| 4 | Cleaning Bathroom  | Weekly          |
| 5 | Buying Groceries   | Weekly          |

---

## How to Run

1. Make sure Python is installed on your system
2. Clone or download this repository
3. Run the program using:

```bash
python chore_tracker.py
```

4. Follow the prompts in the terminal

---

## Example Output

The program displays:

* Room number and room monitor
* Assigned chores with corresponding roommates and status
* Total completed and assigned chores
* Completion rate
* Final room status

---

## Learning Objectives

* Use variables and appropriate data types
* Apply loops for repetitive tasks
* Store and retrieve data using lists
* Implement conditional logic for decision-making
* Perform manual input validation
* Format outputs for readability

---

## File Structure

```
chore_tracker.py   # Main program file
README.md          # Project documentation
```

---

## Author

John Joram Carmelotes

---

## Notes

This project is designed for educational purposes and follows beginner-friendly Python practices without using advanced built-in validation functions.
