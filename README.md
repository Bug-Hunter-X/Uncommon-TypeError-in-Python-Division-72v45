# Uncommon TypeError in Python Division

This repository demonstrates a rather uncommon `TypeError` that can occur in Python when performing division.  The error arises not from a simple `ZeroDivisionError`, but from attempting to divide a number by a string. This example showcases robust error handling and also highlights why type checking is important when designing Python functions.

## Bug Description
The `bug.py` file contains a function that attempts to handle division by zero and type errors. However, if you provide a string as the divisor, the error is not a `ZeroDivisionError`, but instead a `TypeError` indicating incompatible operand types for division. 

## Solution
The `bugSolution.py` file offers a more thorough approach to handling potential errors during division. This includes more precise type checking or using a `try-except` block to catch various exceptions during the process.