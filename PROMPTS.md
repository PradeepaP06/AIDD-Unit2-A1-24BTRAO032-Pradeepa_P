Prompt Engineering Practicum

Student Expense Splitter CLI

AI Coding Assistant: Cursor
Model: Grok 4.6 Medium

---

1. Zero-Shot Prompting

Prompt

I want to develop a Student Expense Splitter CLI application using Python.

Create a command-line application that allows students to manage shared expenses. The application should support adding expenses, viewing expenses, calculating total expenses, calculating equal shares, determining who owes or receives money, and removing expenses.

Organize the project into separate modules for expense management, expense splitting, and CLI functionality. Include input validation and handle rounding errors when expenses cannot be divided equally.

Use clean, beginner-friendly Python code and follow good coding practices.

---

2. Few-Shot Prompting

Prompt

We need to verify that the balance calculation in the Student Expense Splitter is correct for expenses with different numbers of participants.

Follow the existing project structure and testing conventions.

Examples:

Example 1: Equal division

Expense: ₹100
Participants: Alice and Bob

Expected result:

- Alice: ₹50
- Bob: ₹50

Example 2: Unequal division

Expense: ₹100
Participants: Alice, Bob, and Charlie

Expected result:

- Each participant's share should be calculated correctly.
- The total of all shares must equal ₹100.

Example 3: Four participants

Expense: ₹100
Participants: Alice, Bob, Charlie, and David

Expected result:

- Each participant should receive a correctly calculated share.
- The balances should sum to zero.

Use these examples as guidance to create test cases for expense splitting, including amounts that cannot be divided evenly.

---

3. Chain-of-Thought Prompting

Prompt

Analyze the balance calculation in the Student Expense Splitter step by step.

Consider the following edge cases:

1. Expenses shared by two participants.
2. Expenses shared by three or four participants.
3. Amounts that cannot be divided evenly.
4. Participants who paid different amounts.
5. Balances that should sum to zero.
6. Rounding errors involving cents.

Identify possible calculation errors, explain their causes, suggest corrections, and create appropriate pytest test cases.

Do not change unrelated parts of the project. Run the tests after making the changes and report the results.

---

Conclusion

Zero-Shot prompting was used to generate the initial project functionality.

Few-Shot prompting was used to guide the AI using examples of expense splitting and expected results.

Chain-of-Thought prompting was used to analyze calculation logic, identify edge cases, debug errors, and improve testing.