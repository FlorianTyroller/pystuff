def process_text_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        modified_lines = []
        for line in lines:
            if ':' in line:
                line = line.replace(':', ':\n')
            modified_lines.append(line)
        
        with open(filename, 'w') as file:
            file.writelines(modified_lines)
        
        print("Text file processed successfully.")
    except FileNotFoundError:
        print("File not found.")


# Example usage:
filename = "tools/idleon/save.txt"
process_text_file(filename)