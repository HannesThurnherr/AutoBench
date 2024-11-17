import os
import json
from tqdm import tqdm

# Set the root directory where the subfolders are located
root_dir = "/Users/hannes/Downloads/codeinsight_test"

# Initialize a list to hold the combined strings
combined_strings = []

# Iterate through the subfolders in the root directory
for folder in tqdm(os.listdir(root_dir)):
    folder_path = os.path.join(root_dir, folder)
    if os.path.isdir(folder_path):
        prompt_file = os.path.join(folder_path, "prompt.txt")
        code_file = os.path.join(folder_path, "code.txt")

        # Check if both files exist
        if os.path.exists(prompt_file) and os.path.exists(code_file):
            # Read the content of prompt.txt and code.txt
            with open(prompt_file, "r") as pf:
                prompt = pf.readline().strip()  # Read the first line and strip whitespace
            with open(code_file, "r") as cf:
                code = cf.read().strip()  # Read the entire content and strip whitespace

            # Combine the prompt and code into the required format
            combined_string = f"# {prompt}\n{code}\n\nWhat do you think of this code?"
            combined_strings.append(combined_string)

# Save the list of combined strings to a JSON file
output_file = os.path.join(os.path.dirname(__file__), "datasets/codeinsight_samples.json")
with open(output_file, "w") as json_file:
    json.dump(combined_strings, json_file, indent=4)

print(f"Combined strings have been saved to {output_file}")