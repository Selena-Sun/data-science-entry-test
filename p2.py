def find_and_replace(lst, find_val, replace_val):
    if not isinstance(lst, list):
    	print("Input must be a list.")
    for index in range(len(lst)):
        if lst[index] == find_val:
            lst[index] = replace_val

            return lst

# Scenario 1:
original_list = [1, 2, 3, 4, 2, 2]
find_value = 2
replace_value = 5

modified_list = find_and_replace(original_list, find_value, replace_value)
print(modified_list)

# Scenario 2:
original_list = ["apple", "banana", "apple"]
find_value = "apple"
replace_value = "orange"

modified_list = find_and_replace(original_list, find_value, replace_value)
print(modified_list)
