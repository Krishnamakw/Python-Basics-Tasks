# Task 6: Using the Math Module for Calculations

import math

# Ask the user for a number
number = float(input("Enter a number: "))

# Perform calculations using math module
square_root = math.sqrt(number)
natural_log = math.log(number)
sine_value = math.sin(number)

# Display the results
print(f"\nResults for number {number}:")
print(f"Square Root: {square_root}")
print(f"Natural Logarithm (ln): {natural_log}")
print(f"Sine (in radians): {sine_value}")
