import os
import datasets
import json
import random
import re
random.seed(42)
import copy
O = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

examples_num = 5

# name = "gsm8k"
# datas = datasets.load_dataset(name, 'main', split='test')
# datas_ = [
#     {
#         "question": d['question'],
#         "answer": d['answer'].split('####')[-1].strip(),
#         "reference": d['answer'].split('####')[0].strip()
#     } for d in datas
# ]
# random.shuffle(datas_)
# print(name, len(datas_)-examples_num)
# json.dump(datas_[:examples_num], open(f'datas/examples/{name}_examples.json', 'w'), ensure_ascii=False, indent=4)
# json.dump(datas_[examples_num:], open(f'datas/raw_datas/{name}_raw.json', 'w'), ensure_ascii=False, indent=4)

# name = "csqa"
# datas = datasets.load_dataset("commonsense_qa", split='validation')
# datas_ = [
#     {
#         "question": d['question'] + " Choose from: " + ", ".join([l+'. '+t for l, t in zip(d['choices']['label'], d['choices']['text'])]), 
#         "answer": d['answerKey'] + '. ' + d['choices']['text'][d['choices']['label'].index(d['answerKey'])]
#     } for d in datas
# ]
# random.shuffle(datas_)
# print(name, len(datas_)-examples_num)
# json.dump(datas_[:examples_num], open(f'datas/examples/{name}_examples.json', 'w'), ensure_ascii=False, indent=4)
# json.dump(datas_[examples_num:], open(f'datas/raw_datas/{name}_raw.json', 'w'), ensure_ascii=False, indent=4)

# name = "truthfulqa"
# datas = json.load(open(f'datas/raw_datas/{name}.json', 'r'))['examples']
# random.shuffle(datas)
# datas_ = []
# for d in datas:
#     choices = list(d['target_scores'].keys())
#     gold = [k for k, v in d['target_scores'].items() if v == 1][0]
#     random.shuffle(choices)
#     datas_.append({
#         "question": d['input'].strip() + " Choose from:\n" + "\n".join([l+'. '+t for l, t in zip(O[:len(choices)], choices)]),
#         "answer": [l for l, t in zip(O[:len(choices)], choices) if t == gold][0] + '. ' + gold
#     })
# print(name, len(datas_)-examples_num)
# json.dump(datas_[:examples_num], open(f'datas/examples/{name}_examples.json', 'w'), ensure_ascii=False, indent=4)
# json.dump(datas_[examples_num:], open(f'datas/raw_datas/{name}_raw.json', 'w'), ensure_ascii=False, indent=4)

# name = "hellaswag"
# datas = datasets.load_dataset(name, split='validation')
# datas_ = [
#     {
#         "question": "Finish the sentence.\n" + d['ctx'] + " ? Choose from: " + ', '.join([l+'. '+t for l, t in zip(O[:len(d['endings'])], d['endings'])]), 
#         "answer": O[int(d['label'])]
#     } for d in datas
# ]
# random.shuffle(datas_)
# print(name, len(datas_)-examples_num)
# json.dump(datas_[:examples_num], open(f'datas/examples/{name}_examples.json', 'w'), ensure_ascii=False, indent=4)
# json.dump(datas_[examples_num:], open(f'datas/raw_datas/{name}_raw.json', 'w'), ensure_ascii=False, indent=4)

# name = "arceasy"
# datas = datasets.load_dataset("ai2_arc", "ARC-Easy", split='test')
# datas_ = [
#     {
#         "question": d['question'] + " Choose from: " + ", ".join([l+'. '+t for l, t in zip(d['choices']['label'], d['choices']['text'])]), 
#         "answer": d['answerKey'] + '. ' + d['choices']['text'][d['choices']['label'].index(d['answerKey'])]
#     } for d in datas
# ]
# random.shuffle(datas_)
# print(name, len(datas_)-examples_num)
# json.dump(datas_[:examples_num], open(f'datas/examples/{name}_examples.json', 'w'), ensure_ascii=False, indent=4)
# json.dump(datas_[examples_num:], open(f'datas/raw_datas/{name}_raw.json', 'w'), ensure_ascii=False, indent=4)

# name = "arcchallenge"
# datas = datasets.load_dataset("ai2_arc", "ARC-Challenge", split='test')
# datas_ = [
#     {
#         "question": d['question'] + " Choose from: " + ", ".join([l+'. '+t for l, t in zip(d['choices']['label'], d['choices']['text'])]), 
#         "answer": d['answerKey'] + '. ' + d['choices']['text'][d['choices']['label'].index(d['answerKey'])]
#     } for d in datas
# ]
# random.shuffle(datas_)
# print(name, len(datas_)-examples_num)
# json.dump(datas_[:examples_num], open(f'datas/examples/{name}_examples.json', 'w'), ensure_ascii=False, indent=4)
# json.dump(datas_[examples_num:], open(f'datas/raw_datas/{name}_raw.json', 'w'), ensure_ascii=False, indent=4)

# def help_boxed(s, solution):
#     flag = 0
#     rs = ""
#     for i in range(len(s)):
#         if s[i] == "{":
#             flag += 1
#         if s[i] == "}":
#             flag -= 1
#             if flag == -1:
#                 break
#         rs += s[i]
#     temp = "boxed{" + rs + "}"
#     assert temp in solution
#     return rs
# def check_num(s):
#     if s.isdigit():
#         return True
#     # if s[:8] == "\\cfrac{" and s[-1] == "}":
#     #     return True
#     return False
# datas = [[], [], [], [], []]
# for dir in os.listdir(f'datas/raw_datas/MATH/test'):
#     datas_ = []
#     for file in os.listdir(f'datas/raw_datas/MATH/test/{dir}'):
#         data = json.load(open(f'datas/raw_datas/MATH/test/{dir}/{file}', 'r'))
#         if "boxed" not in data['solution']:
#             continue
#         answer = help_boxed(data['solution'].split('boxed{')[-1], data['solution'])
#         if not check_num(answer):
#             continue
#         data = {
#             "question": data['problem'],
#             "answer": answer,
#             "reference": data['solution'],
#             "level": data['level'],
#             "type": data['type']
#         }
#         if data['level'] == "Level 1":
#             datas_.append(data)
#             datas[0].append(data)
#         elif data['level'] == "Level 2":
#             datas_.append(data)
#             datas[1].append(data)
#         elif data['level'] == "Level 3":
#             datas_.append(data)
#             datas[2].append(data)
#         elif data['level'] == "Level 4":
#             # datas_.append(data)
#             datas[3].append(data)
#         elif data['level'] == "Level 5":
#             # datas_.append(data)
#             datas[4].append(data)
#     random.shuffle(datas_)
#     print(len(datas_)-examples_num)
#     json.dump(datas_[:examples_num], open(f'datas/examples/math_{dir}_examples.json', 'w'), ensure_ascii=False, indent=4)
#     json.dump(datas_[examples_num:], open(f'datas/raw_datas/math_{dir}_raw.json', 'w'), ensure_ascii=False, indent=4)
# for i in range(5):
#     random.shuffle(datas[i])
#     print(i, len(datas[i])-examples_num)
#     json.dump(datas[i][:examples_num], open(f'datas/examples/math{i+1}_examples.json', 'w'), ensure_ascii=False, indent=4)
#     json.dump(datas[i][examples_num:], open(f'datas/raw_datas/math{i+1}_raw.json', 'w'), ensure_ascii=False, indent=4)

# names = {
#     "stem": [
#         "abstract_algebra",
#         "anatomy",
#         "astronomy",
#         "college_biology",
#         "college_chemistry",
#         "college_computer_science",
#         "college_mathematics",
#         "college_physics",
#         "computer_security",
#         "conceptual_physics",
#         "electrical_engineering",
#         "elementary_mathematics",
#         "high_school_biology",
#         "high_school_chemistry",
#         "high_school_computer_science",
#         "high_school_mathematics",
#         "high_school_physics",
#         "high_school_statistics",
#         "machine_learning",
#     ],
#     'other': [
#         "business_ethics",
#         "clinical_knowledge",
#         "college_medicine",
#         "global_facts",
#         "human_aging",
#         "management",
#         "marketing",
#         "medical_genetics",
#         "miscellaneous",
#         "nutrition",
#         "professional_accounting",
#         "professional_medicine",
#         "virology",
#     ],
#     "social": [
#         "econometrics",
#         "high_school_geography",
#         "high_school_government_and_politics",
#         "high_school_macroeconomics",
#         "high_school_microeconomics",
#         "high_school_psychology",
#         "human_sexuality",
#         "professional_psychology",
#         "public_relations",
#         "security_studies",
#         "sociology",
#         "us_foreign_policy",
#     ],
#     "human": [
#         "formal_logic",
#         "high_school_european_history",
#         "high_school_us_history",
#         "high_school_world_history",
#         "international_law",
#         "jurisprudence",
#         "logical_fallacies",
#         "moral_disputes",
#         "moral_scenarios",
#         "philosophy",
#         "prehistory",
#         "professional_law",
#         "world_religions",
#     ]
# }
# for name in list(names.keys()):
#     datas_ = []
#     for name_ in names[name]:
#         datas = datasets.load_dataset("cais/mmlu", name_, split="test")
#         for data in datas:
#             datas_.append({
#                 "question": data['question'] + " Choose from: " + ", ".join([l+'. '+t for l, t in zip(O[:len(data['choices'])], data['choices'])]),
#                 "answer": O[data['answer']] + '. ' + data['choices'][data['answer']],
#                 "subject": data['subject']
#             })        
#     random.shuffle(datas_)
#     print(name, len(datas_)-examples_num)
#     json.dump(datas_[:examples_num], open(f'datas/examples/mmlu{name}_examples.json', 'w'), ensure_ascii=False, indent=4)
#     json.dump(datas_[examples_num:], open(f'datas/raw_datas/mmlu{name}_raw.json', 'w'), ensure_ascii=False, indent=4)

################################################################################################################################
################################################################################################################################
# datas = json.load(open('datas/raw_datas/coin_flip.json', 'r'))["examples"]
# json.dump(datas[3:], open('datas/raw_datas/coin_raw.json', 'w'), ensure_ascii=False)

# datas = datasets.load_dataset('tasksource/bigbench', 'tracking_shuffled_objects', split='validation')
# datas = [{
#         "question": d['inputs'] + ' ?', 
#         "answer": d['targets'][0]
#     } for d in datas]
# json.dump(datas[3:], open('datas/raw_datas/tracking5_raw.json', 'w'), ensure_ascii=False)

# datas = json.load(open('datas/raw_datas/tracking3.json', 'r'))['examples']
# datas = [{
#         "question": d['input'] + ' ?', 
#         "answer": [k for k, v in d['target_scores'].items() if v == 1][0]
#     } for d in datas]
# print("tracking3", len(datas))
# json.dump(datas[3:], open('datas/raw_datas/tracking3_raw.json', 'w'), ensure_ascii=False)

# datas = json.load(open('datas/raw_datas/last_letters.json', 'r'))['examples']
# datas = [{
#         "question": d['question'], 
#         "answer": "the answer is " + d['answer']
#     } for d in datas]
# print("letter", len(datas))
# json.dump(datas[3:], open('datas/raw_datas/letter_raw.json', 'w'), ensure_ascii=False)

# datas = datasets.load_dataset('tasksource/bigbench', 'date_understanding', split='validation')
# datas = [{
#         "question": d['inputs'].replace("Q: ", "").replace(" A: ", "").replace(" in MM/DD/YYYY", ""), 
#         "answer": "the anwer is " + d['targets'][0]
#     } for d in datas]
# json.dump(datas[3:], open('datas/raw_datas/date_raw.json', 'w'), ensure_ascii=False)

# datas = datasets.load_dataset('ChilleD/MultiArith', split='test')
# datas = [{
#         "question": d['question'], 
#         "answer": "the anwer is " + d['final_ans']
#     } for d in datas]
# print("multiarith", len(datas))
# json.dump(datas[3:], open('datas/raw_datas/multiarith_raw.json', 'w'), ensure_ascii=False)

##############################################################################################################
##############################################################################################################
# name = "categories"
# datas = json.load(open(f'datas/raw_datas/{name}.json', 'r'))['examples']
# for d in datas:
#     if type(d['target']) == list:
#         d['target'] = d['target'][0]
# all_targets = [d['target'].strip() for d in datas]
# all_targets = list(set(all_targets))
# datas_ = []
# random.shuffle(datas)
# for d in datas:
#     C = copy.deepcopy(all_targets)
#     C.remove(d['target'].strip())
#     C = random.sample(C, 3) + [d['target'].strip()]
#     random.shuffle(C)
#     Q = d['input'].strip() + ' ?' + ' Choose from: ' + ', '.join([l+'. '+t for l, t in zip(O[:len(C)], C)])
#     A = O[C.index(d['target'].strip())]
#     datas_.append({
#         "question": Q,
#         "answer": A + '. ' + d['target'].strip()
#     })
# print(name, len(datas_)-3)
# json.dump(datas_[:3], open(f'datas/examples/{name}_examples.json', 'w'), ensure_ascii=False, indent=4)
# json.dump(datas_[3:], open(f'datas/raw_datas/{name}_raw.json', 'w'), ensure_ascii=False, indent=4)

# name = "Chinese"
# datas = json.load(open(f'datas/raw_datas/{name}.json', 'r'))['examples']
# random.shuffle(datas)
# datas_ = []
# for d in datas:
#     datas_.append({
#         "question": d['input'].strip() ,
#         "answer": d['target'].strip()
#     })
# print(name, len(datas_)-3)
# json.dump(datas_[:3], open(f'datas/examples/{name}_examples.json', 'w'), ensure_ascii=False, indent=4)
# json.dump(datas_[3:], open(f'datas/raw_datas/{name}_raw.json', 'w'), ensure_ascii=False, indent=4)

# name = "com2sense"
# datas = json.load(open(f'datas/raw_datas/{name}.json', 'r'))['examples']
# random.shuffle(datas)
# datas_ = []
# for d in datas:
#     datas_.append({
#         "question": d['sent'].strip() + " This statement is True or False?",
#         "answer": d['label'].strip()
#     })
# print(name, len(datas_)-3)
# json.dump(datas_[:3], open(f'datas/examples/{name}_examples.json', 'w'), ensure_ascii=False, indent=4)
# json.dump(datas_[3:], open(f'datas/raw_datas/{name}_raw.json', 'w'), ensure_ascii=False, indent=4)

# name = "date"
# datas = json.load(open(f'datas/raw_datas/{name}.json', 'r'))['examples']
# random.shuffle(datas)
# datas_ = []
# for d in datas:
#     choices = list(d['target_scores'].keys())
#     gold = [k for k, v in d['target_scores'].items() if v == 1][0]
#     random.shuffle(choices)
#     datas_.append({
#         "question": d['input'].strip() + " Choose from: " + ", ".join([l+'. '+t for l, t in zip(O[:len(choices)], choices)]),
#         "answer": [l for l, t in zip(O[:len(choices)], choices) if t == gold][0] + '. ' + gold
#     })
# print(name, len(datas_)-3)
# json.dump(datas_[:3], open(f'datas/examples/{name}_examples.json', 'w'), ensure_ascii=False, indent=4)
# json.dump(datas_[3:], open(f'datas/raw_datas/{name}_raw.json', 'w'), ensure_ascii=False, indent=4)

# name = "intent"
# task_prefix = "Predict the intent of the utterance. The possible choices for the intents are: add_to_playlist, book_restaurant, get_weather, play_music, search_screening_event, search_creative_work, and rate_book.\n\n"
# datas = json.load(open(f'datas/raw_datas/{name}.json', 'r'))['examples']
# random.shuffle(datas)
# datas_ = []
# for d in datas:
#     gold = [k for k, v in d['target_scores'].items() if v == 1][0]
#     datas_.append({
#         "question": task_prefix + d['input'].strip() ,
#         "answer": gold
#     })
# print(name, len(datas_)-3)
# json.dump(datas_[:3], open(f'datas/examples/{name}_examples.json', 'w'), ensure_ascii=False, indent=4)
# json.dump(datas_[3:], open(f'datas/raw_datas/{name}_raw.json', 'w'), ensure_ascii=False, indent=4)

# name = "movie"
# datas = json.load(open(f'datas/raw_datas/{name}.json', 'r'))['examples']
# random.shuffle(datas)
# datas_ = []
# for d in datas:
#     choices = list(d['target_scores'].keys())
#     gold = [k for k, v in d['target_scores'].items() if v == 1][0]
#     random.shuffle(choices)
#     datas_.append({
#         "question": d['input'].strip(':') + ". Recommend a movie similar to the given list of movies. Choose from: " + ", ".join([l+'. '+t for l, t in zip(O[:len(choices)], choices)]),
#         "answer": [l for l, t in zip(O[:len(choices)], choices) if t == gold][0] + '. ' + gold
#     })
# print(name, len(datas_)-3)
# json.dump(datas_[:3], open(f'datas/examples/{name}_examples.json', 'w'), ensure_ascii=False, indent=4)
# json.dump(datas_[3:], open(f'datas/raw_datas/{name}_raw.json', 'w'), ensure_ascii=False, indent=4)

# name = "narrative"
# datas = json.load(open(f'datas/raw_datas/{name}.json', 'r'))['examples']
# random.shuffle(datas)
# datas_ = []
# for d in datas:
#     choices = list(d['target_scores'].keys())
#     gold = [k for k, v in d['target_scores'].items() if v == 1][0]
#     random.shuffle(choices)
#     datas_.append({
#         "question": d['input'].strip() + "\nGiven narrative above and choose the most related proverb from:\n" + "\n".join([l+'. '+t for l, t in zip(O[:len(choices)], choices)]),
#         "answer": [l for l, t in zip(O[:len(choices)], choices) if t == gold][0] + '. ' + gold
#     })
# print(name, len(datas_)-3)
# json.dump(datas_[:3], open(f'datas/examples/{name}_examples.json', 'w'), ensure_ascii=False, indent=4)
# json.dump(datas_[3:], open(f'datas/raw_datas/{name}_raw.json', 'w'), ensure_ascii=False, indent=4)

# name = "object"
# datas = json.load(open(f'datas/raw_datas/{name}.json', 'r'))['examples']
# random.shuffle(datas)
# datas_ = []
# for d in datas:
#     if "objects" not in d['input']:
#         datas_.append({
#             "question": d['input'],
#             "answer": d['target'][-1]
#         })
# print(name, len(datas_)-3)
# json.dump(datas_[:3], open(f'datas/examples/{name}_examples.json', 'w'), ensure_ascii=False, indent=4)
# json.dump(datas_[3:], open(f'datas/raw_datas/{name}_raw.json', 'w'), ensure_ascii=False, indent=4)

# name = "odd"
# datas = json.load(open(f'datas/raw_datas/{name}.json', 'r'))['examples']
# random.shuffle(datas)
# datas_ = []
# for d in datas:
#     choices = list(d['target_scores'].keys())
#     gold = [k for k, v in d['target_scores'].items() if v == 1][0]
#     random.shuffle(choices)
#     datas_.append({
#         "question": d['input'] ,
#         "answer": gold
#     })
# print(name, len(datas_)-3)
# json.dump(datas_[:3], open(f'datas/examples/{name}_examples.json', 'w'), ensure_ascii=False, indent=4)
# json.dump(datas_[3:], open(f'datas/raw_datas/{name}_raw.json', 'w'), ensure_ascii=False, indent=4)

# name = "physical"
# datas = json.load(open(f'datas/raw_datas/{name}.json', 'r'))['examples']
# random.shuffle(datas)
# datas_ = []
# for d in datas:
#     choices = list(d['target_scores'].keys())
#     gold = [k for k, v in d['target_scores'].items() if v == 1][0]
#     random.shuffle(choices)
#     datas_.append({
#         "question": d['input'].strip() + " Choose from: " + ", ".join([l+'. '+t for l, t in zip(O[:len(choices)], choices)]),
#         "answer": [l for l, t in zip(O[:len(choices)], choices) if t == gold][0] + '. ' + gold
#     })
# print(name, len(datas_)-3)
# json.dump(datas_[:3], open(f'datas/examples/{name}_examples.json', 'w'), ensure_ascii=False, indent=4)
# json.dump(datas_[3:], open(f'datas/raw_datas/{name}_raw.json', 'w'), ensure_ascii=False, indent=4)

# name = "rhyme"
# datas = json.load(open(f'datas/raw_datas/{name}.json', 'r'))['examples']
# random.shuffle(datas)
# datas_ = []
# for d in datas:
#     choices = list(d['target_scores'].keys())
#     gold = [k for k, v in d['target_scores'].items() if v == 1][0]
#     random.shuffle(choices)
#     datas_.append({
#         "question": d['input'].strip() + "\nGiven word above and choose a word with same rhyme from: " + ", ".join([l+'. '+t for l, t in zip(O[:len(choices)], choices)]),
#         "answer": [l for l, t in zip(O[:len(choices)], choices) if t == gold][0] + '. ' + gold
#     })
# print(name, len(datas_)-3)
# json.dump(datas_[:3], open(f'datas/examples/{name}_examples.json', 'w'), ensure_ascii=False, indent=4)
# json.dump(datas_[3:], open(f'datas/raw_datas/{name}_raw.json', 'w'), ensure_ascii=False, indent=4)


# name = "sequence"
# datas = json.load(open(f'datas/raw_datas/{name}.json', 'r'))['examples']
# random.shuffle(datas)
# datas_ = []
# for d in datas:
#     choices = list(d['target_scores'].keys())
#     gold = [k for k, v in d['target_scores'].items() if v == 1][0]
#     random.shuffle(choices)
#     if len(gold.split(', ')[0]) == 1:
#         continue
#     datas_.append({
#         "question": d['input'].strip() + " Choose from:\n" + "\n".join([l+'. '+t for l, t in zip(O[:len(choices)], choices)]),
#         "answer": [l for l, t in zip(O[:len(choices)], choices) if t == gold][0] + '. ' + gold
#     })
# print(name, len(datas_)-3)
# json.dump(datas_[:3], open(f'datas/examples/{name}_examples.json', 'w'), ensure_ascii=False, indent=4)
# json.dump(datas_[3:], open(f'datas/raw_datas/{name}_raw.json', 'w'), ensure_ascii=False, indent=4)

# name = "sort"
# datas = json.load(open(f'datas/raw_datas/{name}.json', 'r'))['examples']
# random.shuffle(datas)
# datas_ = []
# for d in datas:
#     if len(d['input'].split(' ')) == 4:
#         datas_.append({
#             "question": "Sort the following words alphabetically:\n" + d['input'].strip(),
#             "answer": d['target'].strip()
#         })
# print(name, len(datas_)-3)
# json.dump(datas_[:3], open(f'datas/examples/{name}_examples.json', 'w'), ensure_ascii=False, indent=4)
# json.dump(datas_[3:], open(f'datas/raw_datas/{name}_raw.json', 'w'), ensure_ascii=False, indent=4)

# name = "sports"
# datas = json.load(open(f'datas/raw_datas/{name}.json', 'r'))['examples']
# random.shuffle(datas)
# datas_ = []
# for d in datas:
#     gold = [k for k, v in d['target_scores'].items() if v == 1][0]
#     datas_.append({
#         "question": "Determine whether the following statement or statements are plausible or implausible:\n" + d['input'].strip(),
#         "answer": gold.strip()
#     })
# print(name, len(datas_)-3)
# json.dump(datas_[:3], open(f'datas/examples/{name}_examples.json', 'w'), ensure_ascii=False, indent=4)
# json.dump(datas_[3:], open(f'datas/raw_datas/{name}_raw.json', 'w'), ensure_ascii=False, indent=4)