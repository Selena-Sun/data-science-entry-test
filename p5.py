def check_divisibility(num, divisor):

    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        raise ValueError("Both num and divisor must be numeric.")

    return num % divisor == 0

# Scenario 1: Check divisibility of 10 by 2
result1 = check_divisibility(10, 2)
print(result1)

# Scenario 2: Check divisibility of 7 by 3
result2 = check_divisibility(7, 3)
print(result2)
