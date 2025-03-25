def find_first_negative(lst):

    index = 0
    while index < len(lst):
        if lst[index] < 0:
            return lst[index]
        index += 1
    
    return "No negatives"

# Scenario 1: Finding the first negative in [3, 5, -1, 7, -2, 8]
result1 = find_first_negative([3, 5, -1, 7, -2, 8])
print(result1)

# Scenario 2: Finding the first negative in [2, 10, 7, 0]
result2 = find_first_negative([2, 10, 7, 0])
print(result2)
