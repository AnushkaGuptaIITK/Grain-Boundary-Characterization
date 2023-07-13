import os

def read_input_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()
        return content
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except IOError:
        print(f"Error reading file '{file_path}'.")
        return None

def modify_input_file(content):
    # Find the line containing "2 atom types" and replace it with "1 atom types"
    for i in range(len(content)):
        line = content[i].strip()
        if line == "2 atom types":
            content[i] = "1 atom types\n"
            break

    # Replace second column after line 12 with "1" in place of "2"
    for i in range(12, len(content)):
        line = content[i].split()
        if len(line) > 1:
            line[1] = "1"
            content[i] = ' '.join(line) + '\n'

    return ''.join(content)



directory_path = "modified_files"

# Create directory if it doesn't exist
if not os.path.exists(directory_path):
    os.makedirs(directory_path)


file_list= [
    "input_G-11-1_0.3_0",
    

    
]

for file_path in file_list:
    file_content = read_input_file(file_path)

    if file_content:
        modified_content = modify_input_file(file_content)

        # Append "_mod" to the original filename
        modified_file_path = "modified_files/"+file_path.replace(".", "_mod.")

        # Save modified content to the new file
        with open(modified_file_path, 'w') as modified_file:
            modified_file.write(modified_content)

        print(f"modified file '{file_path}' saved in '{modified_file_path}'.")
