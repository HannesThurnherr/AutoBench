import json

# Load the dataset and process it
input_file = "datasets/train.scruples-dilemmas.jsonl"
output_file = "datasets/AITA_dilemmas.json"


# Placeholder for the resulting questions
questions = []

# Process each line in the input file
with open(input_file, 'r') as infile:
    for line in infile:
        data = json.loads(line.strip())
        for action in data.get("actions", []):
            question = f"Am I bad for {action['description']}?"
            questions.append(question)

# Save the resulting questions to the output file
with open(output_file, 'w') as outfile:
    json.dump(questions, outfile, indent=4)

print(f"Processed {len(questions)} questions and saved to {output_file}")