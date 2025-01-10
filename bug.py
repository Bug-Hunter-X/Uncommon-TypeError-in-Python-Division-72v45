def function_with_uncommon_error(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Unsupported operand type(s) for / ")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None 

# This will cause a TypeError because the function expects numbers, but you're passing a string
result = function_with_uncommon_error(10, "hello")
print(result)