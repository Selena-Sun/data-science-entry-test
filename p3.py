def update_dictionary(dct, key, value):

    if key in dct:
        print(f"Original value: {dct[key]}")
    dct[key] = value
    return dct

# Scenario 1: Updating an empty dictionary
result1 = update_dictionary({}, "name", "Alice")
print(result1)

# Scenario 2: Updating a dictionary with an existing key
result2 = update_dictionary({"age": 25}, "age", 26)
print(result2)
