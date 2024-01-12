# Initializing global variable
global_variable = 100

# Initializing a dictionary
my_dict = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}

# Defining function to process data
def process_data():
    global global_variable
    local_variable = 5
    
    # Initializing a list
    data_list = [1, 2, 3, 4, 5]

    # Loop while the local variable is greater than 0
    while local_variable > 0:
        # Check if the global variable is even
        if global_variable % 2 == 0:
            # Append the global variable to the list
            data_list.append(global_variable)
        
        # Decrement the local variable
        local_variable -= 1

    # Return the processed list
    return data_list

# Initialize a set
my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}

# Call the function and store the result
result_list = process_data()

# Define a function to modify the dictionary
def modify_dict():
    # Initialize a local variable
    local_variable = 10
    
    # Add a new key-value pair to the dictionary
    my_dict['new_key'] = local_variable

# Call the function to modify the dictionary
modify_dict()

# Define a function to update the global variable
def update_global():
    global global_variable
    global_variable += 10

# Loop through a range
for i in range(5):
    print(i)

# Check conditions and print messages
if my_set is not None and my_dict.get('new_key') == 10:
    print("Condition met!")

if 5 not in my_set:
    print("5 not found in the set!")

print(global_variable)
print(my_dict)
print(my_set)
