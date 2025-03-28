def swap_values(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return -1
    
    x, y = y, x
    
    print(f"Swapped values: x = {x}, y = {y}")

# Scenario 1:
result = swap_values("Apple", 10)
print(result)

# Scenario 2:
result = swap_values(9, 17)
print(result)
