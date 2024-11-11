import json

def extract_question_en(json_data):
    questions = []
    for item in json_data:
        if "question_en" in item:
            questions.append(item["question_en"])
    return questions

# Assuming the JSON data is stored in a file named 'data.json'
with open('question_test.json', 'r', encoding='utf-8') as file:

    data = json.load(file)

question_en_list = extract_question_en(data)

print(len(question_en_list))
