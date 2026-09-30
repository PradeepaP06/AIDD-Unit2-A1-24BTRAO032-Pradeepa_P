# Student Expense Splitter CLI

## Overview

Student Expense Splitter is a Python command-line application designed to manage and split shared expenses between students.

The application allows users to:

- Add an expense
- View all expenses
- Calculate total expenses
- Calculate equal shares
- Calculate who owes or should receive money
- Remove an expense
- Validate expense inputs
- Handle rounding when expenses cannot be divided evenly

## AI Coding Assistant Used

**Tool:** Cursor  
**Model:** Grok 4.6 Medium

Cursor was used during the development of the project to generate the initial application, improve unit tests, and debug expense balance calculations.

## Technologies Used

- Python 3.12
- pytest
- Git
- GitHub
- Cursor

## Project Structure

```text
student-expense-splitter/
│
├── src/
│   ├── __init__.py
│   ├── cli.py
│   ├── expense.py
│   └── splitter.py
│
├── tests/
│   ├── conftest.py
│   ├── test_expense.py
│   ├── test_splitter.py
│   └── test_validation_and_splitting.py
│
├── README.md
├── requirements.txt
└── .gitignore
