# Task 5: Calculate Factorial Using a Function

# Define a function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Call the function with a sample number
sample_number = 5
fact = factorial(sample_number)

# Print the result
print(f"The factorial of {sample_number} is: {fact}")
