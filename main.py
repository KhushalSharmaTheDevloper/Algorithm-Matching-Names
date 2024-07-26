import time as t

print('Program Successfully Started.')

name = 'Khushal Sharma'
name2 = 'Deepak Sharma'

def training():
    global name2

    # Print the initial values
    print(f'Initial name2: {name2}')

    # Convert strings to lists for character-wise manipulation
    name_list = list(name)
    name2_list = list(name2)

    iteration_count = 0
    max_iterations = 100  # Set a reasonable limit to prevent infinite loops

    while iteration_count < max_iterations:
        # Check if name2 matches name
        if name_list == name2_list[:len(name_list)]:
            print('name2 has been updated to match name.')
            break

        # Adjust name2_list to match name_list
        if len(name2_list) < len(name_list):
            # Add characters if name2_list is shorter
            for i in range(len(name2_list), len(name_list)):
                name2_list.append(name_list[i])
                print(f'Added: {name_list[i]} -> name2: {"".join(name2_list)}')
        elif len(name2_list) > len(name_list):
            # Remove characters if name2_list is longer
            while len(name2_list) > len(name_list):
                removed_char = name2_list.pop()
                print(f'Removed: {removed_char} -> name2: {"".join(name2_list)}')
        else:
            # Replace characters if name2_list and name_list are of the same length
            for i in range(len(name_list)):
                if name2_list[i] != name_list[i]:
                    name2_list[i] = name_list[i]
                    print(f'Updated position {i}: {name_list[i]} -> name2: {"".join(name2_list)}')

        # Convert list back to string
        name2 = ''.join(name2_list)
        
        # Add a delay for demonstration purposes
        t.sleep(3)  # Sleep for 1 second

        iteration_count += 1  # Increment iteration count

    if iteration_count >= max_iterations:
        print("Reached maximum iterations. Exiting.")

training()
