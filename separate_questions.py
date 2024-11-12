import json
from collections import defaultdict
from tqdm import tqdm
# Load the JSON data
with open("question_test.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Dictionary to store questions by category
categorized_questions = defaultdict(list)

# Iterate over each entry in the JSON data
for entry in tqdm(data):
    category = entry.get("category")
    question_en = entry.get("question_en")
    if category and question_en:
        categorized_questions[category].append(question_en)

# Save each category's questions into separate JSON files
for category, questions in categorized_questions.items():
    filename = f"{category}_questions.json"
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(questions, file, ensure_ascii=False, indent=4)

print("Categorized questions saved to individual JSON files.")