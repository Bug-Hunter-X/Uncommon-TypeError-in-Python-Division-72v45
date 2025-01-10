def function_with_uncommon_error_solution(x, y):
    try:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Operands must be numbers")
        result = x / y
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# This will now raise a TypeError because of explicit type checking
result = function_with_uncommon_error_solution(10, "hello")
print(result)

# This will execute correctly
result = function_with_uncommon_error_solution(10, 2)
print(result) 