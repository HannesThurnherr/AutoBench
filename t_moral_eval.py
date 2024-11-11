import time
import pickle
import os
import json
import matplotlib.pyplot as plt
from moral_eval import *
from models.OpenAIChatModel import OpenAIChatModel
from models.AnthropicChatModel import AnthropicChatModel


def compare_answers(set1, set2):
    # Counters
    total_questions = len(set1)
    agreement_count = 0
    disagreement_dict = {}

    # Iterate through the questions
    for question, answer1 in set1.items():
        answer2 = set2.get(question)

        # Check if answers agree
        if answer1 == answer2:
            agreement_count += 1
        else:
            # Store the disagreements
            disagreement_dict[question] = {'Set 1': answer1, 'Set 2': answer2}

    # Calculate the percentage of agreement
    agreement_percentage = (agreement_count / total_questions) * 100

    return agreement_percentage, disagreement_dict


#claude_35 = AnthropicChatModel("claude-3-5-sonnet-20240620")
#gpt_4o = OpenAIChatModel("gpt-4o")


with open("questionaire_lie_honest.pkl", "rb") as f:
    questionaire = pickle.load(f)

#claude_35_answers = apply_questionaire_chat_model(questionaire, claude_35)
"""with open("claude_35_answers.pkl", "wb") as f:
    pickle.dump(claude_35_answers, f)
"""

"""
with open("claude_35_answers.pkl", "rb") as f:
    claude_answers = pickle.load(f)

alph = ["A", "B", "C"]
with open("gpt_4o_answers.pkl", "rb") as f:
    gpt_answers = pickle.load(f)
#visualize_answers(answers,options)

#visualize_answers(apply_questionaire_chat_model(questionaire, gpt_4o, verbose=True), options)

agreement_percentage, disagreements = compare_answers(claude_answers, gpt_answers)

print(f"{agreement_percentage} of the answers are the same")

for i in disagreements.keys():
    print(i)
    counter = 0
    for j in questionaire[i].keys():
        print(alph[counter] ,questionaire[i][j])
        counter += 1
    print(f"claude sais: {disagreements[i]['Set 1']}")
    print(f"gpt sais: {disagreements[i]['Set 2']}")
"""

for i in questionaire.keys():
    print(i)
    for j in questionaire[i].keys():
        print("    ",j,":",questionaire[i][j])

