# Unit Conversion System

A simple Python project that converts units using a menu-driven program.

## Features

-   **Length:** Kilometers (km) to Miles
-   **Weight:** Kilograms (kg) to Grams
-   **Temperature:** Celsius (°C) to Fahrenheit (°F)
-   **Time:** Hours to Minutes
-   Repeats the menu until the user chooses Exit
-   Handles invalid menu choices and non-numeric input

## Requirements

-   Python 3

No additional libraries are required.

## How to Run

1.  Save the program in a file named `unit_conversion.py`.

2.  Open a terminal or command prompt in that folder.

3.  Run:

    ``` bash
    python unit_conversion.py
    ```

    If your system uses `python3`, run:

    ``` bash
    python3 unit_conversion.py
    ```

## How to Use

1.  Run the program.
2.  Select an option from `1` to `4`.
3.  Enter the value you want to convert.
4.  Read the converted result.
5.  Enter `0` to exit the program.

## Conversion Formulas

  Conversion              Formula
  ----------------------- ---------------------
  Kilometers to Miles     `km × 0.621371`
  Kilograms to Grams      `kg × 1000`
  Celsius to Fahrenheit   `(°C × 9 / 5) + 32`
  Hours to Minutes        `hours × 60`

## Example

``` text
--- UNIT CONVERSION SYSTEM ---
1. Length (KM to Miles)
2. Weight (KG to Grams)
3. Temperature (C to F)
4. Time (Hours to Minutes)
0. Exit
Enter choice: 1
Enter value: 10
10 km = 6.21 miles
```

## Concepts Used

-   Python functions
-   `while` loop
-   `if`, `elif`, and `else` conditions
-   User input with `input()`
-   Type conversion with `float()`
-   Error handling with `try` and `except`
-   Formatted strings (f-strings)

## Author

Created as a beginner-friendly Python project.
