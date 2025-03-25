def string_reverse(s):

    if not isinstance(s, str):
        raise ValueError("Input must be a string.")

    return s[::-1]

# Scenario 1: Reversing "Hello World"
result1 = string_reverse("Hello World")
print(result1)

# Scenario 2: Reversing "Python"
result2 = string_reverse("Python")
print(result2)
