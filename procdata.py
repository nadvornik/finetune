import os
import json

# Create a JSON dataset from a directory containing
# short files. The length of individual files should
# not exceed model context size (4096 tokens).

# Define the directory path to read files from
directory_path = "dataset"

# Initialize a list to store file contents
file_contents = []

# Iterate through all files in the directory
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    
    # Check if the item is a file
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            file_contents.append({"text" : content})

# Define the name of the output JSON file
output_json_file = "dataset.json"

# Write the file contents to a JSON file
with open(output_json_file, "w") as json_file:
    json.dump(file_contents, json_file, indent=4)

print(f"File contents saved to {output_json_file}")