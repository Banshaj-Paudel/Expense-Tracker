# Expense Tracker

Expense Tracker is a simple command-line Python application for recording expenses, listing them, grouping them by category, and generating a date-range report.

## Requirements

- Python 3

## Run the project

From the project root:

```bash
python main.py
```

## Available commands

When the app starts, it shows the supported commands:

```text
add <amount> <category>
categorize
display
report <start_date> <end_date>
exit
```

### 1. Add an expense

Adds a new expense with the current date and time.

```text
add 250 food
```

### 2. Display all expenses

Prints every saved expense.

```text
display
```

### 3. Categorize expenses

Groups expenses into these built-in categories:

- `food`
- `bills`
- `fun`
- `loan`

If you use any other category name, it is placed under `other`.

```text
categorize
```

### 4. Generate a report

Shows expenses between a start date and end date.

```text
report 2026-01-01 2026-12-31
```

Use dates in `YYYY-MM-DD` format so they match the stored expense date prefix.

### 5. Exit the application

```text
exit
```

## Example session

```text
Welcome to the Expense Tracker!
Available commands: add <amount> <category>, categorize, display, report <start_date> <end_date>, exit

Enter command: add 100 food
Added expense: Your expense is Rs.100.0 on 2026-09-10 05:44:02. Category: food

Enter command: display
Your expense is Rs.100.0 on 2026-09-10 05:44:02. Category: food
```
