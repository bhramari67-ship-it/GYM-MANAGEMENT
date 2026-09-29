# Gym Management System

A simple beginner-level Python project made for the VITyarthi Python project submission.

## Overview

The Gym Management System is a command-line program that helps a small gym keep basic records. It stores member information, attendance, and payment records in simple text files.

The project focuses on basic Python concepts such as:
- variables and data types
- if-else statements
- loops
- functions
- lists
- classes and objects
- file handling
- exception handling
- basic testing

## Features

- Add a new gym member
- View all members
- Search for a member
- Remove a member
- Mark attendance
- View attendance records
- Add payment details
- View payment records
- Show a simple gym summary

## Project Structure

```text
GymManagementProject/
│
├── main.py
├── member.py
├── member_manager.py
├── attendance.py
├── payment.py
├── report.py
├── README.md
├── statement.md
├── data/
│   ├── members.txt
│   ├── attendance.txt
│   └── payments.txt
│
└── tests/
    └── test_gym.py
```

## Requirements

- Python 3.x
- No external Python packages are required.

## How to Run

1. Download or clone the repository.
2. Open the project folder in VS Code or another Python editor.
3. Open a terminal in the project folder.
4. Run:

```text
python main.py
```

5. Select an option from the menu.

## How to Test

From the project folder, run:

```text
python -m unittest discover -s tests
```

## Data Storage

The project does not use JSON. Member, attendance, and payment records are stored in simple `.txt` files inside the `data` folder.

## GitHub

Create a GitHub repository named something like:

`gym-management-python`

Then upload the complete project folder. The README.md file will automatically appear on the main repository page.
