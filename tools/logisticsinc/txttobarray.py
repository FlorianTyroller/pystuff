import json

def text_to_byte_array(input_file, output_file):
    # Read the text file and convert its content to a byte array
    with open(input_file, 'r') as file:
        text_content = file.read()
        byte_array = [ord(char) for char in text_content]

    # Write the byte array to a JSON file
    with open(output_file, 'w') as json_file:
        json.dump(byte_array, json_file)

# Example usage:
input_file = 'tools/logisticsinc/barraytxt.txt'  # Replace 'input.txt' with the path to your text file
output_file = 'tools/logisticsinc/byteArray.json'  # Output file where the byte array will be saved
text_to_byte_array(input_file, output_file)