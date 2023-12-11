import json

def remove_duplicates(json_data):
    unique_questions = []
    unique_data = []

    for item in json_data:
        question = item["Question"]
        if question not in unique_questions:
            unique_questions.append(question)
            unique_data.append(item)

    return unique_data

# Read JSON data from a file
file_path = "Introducing IT-ITes Industry.json"

with open(file_path, 'r') as file:
    data = json.load(file)

# Remove duplicates
unique_data = remove_duplicates(data)

# Write the unique data back to the file
with open(file_path, 'w') as file:
    json.dump(unique_data, file, indent=2)

print("Duplicate questions removed and saved to the file.")
