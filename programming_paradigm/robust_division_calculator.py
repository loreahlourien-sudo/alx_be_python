def safe_divide(numerator , denominator):
    numerator = float(input("Enter the numerator"))
    denominator = float(input("Enter the denomitor"))
    if denominator == 0:
        return "Error : Division by zero is not allowed."
    result = numerator / denominator
    return result
except ValueError:
return "Error : Non-numeric input provided .Please enter valid numbers ."
