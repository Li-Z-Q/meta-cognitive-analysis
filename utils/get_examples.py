import json
import random
random.seed(0)

def get_other_examples(dir_path, this_dataset_name):
    if this_dataset_name in ["coin", "letter"]:
        examples = [
            random.sample(json.load(open(dir_path + "strategy_examples.json")) + json.load(open(dir_path + "dateu_examples.json")), 1)[0], 
            random.sample(json.load(open(dir_path + "gsm8k_examples.json")) + json.load(open(dir_path + "dateu_examples.json")), 1)[0],
        ]