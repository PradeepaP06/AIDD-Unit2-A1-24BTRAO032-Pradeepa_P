# Prompt Engineering Practicum

## AI Coding Assistant Used
Cursor AI

## Task
Student Expense Tracker CLI application using Python.

---

## 1. Zero-Shot Prompt

### Prompt
Create a Python Student Expense Tracker CLI application.
Implement functions to add expenses, view expenses,
calculate total expenses, calculate category totals,
delete expenses, and display expenses.

Use beginner-friendly Python code, type hints where
appropriate, and input validation.

### Technique
Zero-shot prompting was used because the AI was given
instructions without any examples.

### Decision
Accepted the generated code after reviewing the functions
and checking that they matched the requirements.

---

## 2. Few-Shot Prompt

### Prompt
Create an expense function following these examples:

Example 1:
Input: Food, 150, Food
Output: Expense(name="Food", amount=150.0, category="Food")

Example 2:
Input: Travel, 50, Transport
Output: Expense(name="Travel", amount=50.0, category="Transport")

Example 3:
Input: Books, 500, Education
Output: Expense(name="Books", amount=500.0, category="Education")

Follow the same format and naming conventions.

### Technique
Few-shot prompting was used by providing examples
to guide the AI toward consistent output.

### Decision
Accepted the generated implementation after checking
the output format and consistency.

---

## 3. Chain-of-Thought Prompt

### Prompt
Analyze the expense tracker for these edge cases:

1. Empty expense list
2. Zero expense amount
3. Negative expense amount
4. Invalid expense index
5. Different expense categories

Think step by step, identify possible errors,
suggest fixes, and create unit tests.

### Technique
Chain-of-thought prompting was used for analyzing
edge cases and debugging.

### Decision
Reviewed the suggestions and included validation
and unit tests for important edge cases.

---

## Conclusion

Three prompting techniques were used to develop and
test the Student Expense Tracker. The prompts helped
generate code, maintain consistency, and identify
potential errors.