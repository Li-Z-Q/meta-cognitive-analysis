import json
import random
random.seed(42)

local_facts = {}
global_facts = []
for dataset_name in ["gsm8k", "csqa", "truthfulqa", "arceasy", "arcchallenge", "math1", "math2", "math3", "mmluhuman", "mmluother", "mmlusocial", "mmlustem", "multiarith"]:
    datas = json.load(open(f'datas/datas_with_hint/{dataset_name}_final.json', 'r', encoding='utf-8'))
    local_facts[dataset_name] = []
    for data in datas:
        if dataset_name != "multiarith":
            global_facts += data['factual-hint']
        local_facts[dataset_name] += data['factual-hint']
        
for dataset_name in ["multiarith"]: # ["gsm8k", "csqa", "truthfulqa", "arceasy", "arcchallenge", "math1", "math2", "math3", "mmluhuman", "mmluother", "mmlusocial", "mmlustem"]:
    examples = json.load(open(f'datas/examples/{dataset_name}_examples.json', 'r', encoding='utf-8'))
    examples_w = open(f'datas/examples/{dataset_name}_examples.json', 'w', encoding='utf-8')
    
    datas = json.load(open(f'datas/datas_with_hint/{dataset_name}_final.json', 'r', encoding='utf-8'))
    datas_w = open(f'datas/datas_with_hint/{dataset_name}_final.json', 'w', encoding='utf-8')
    
    for example in examples:
        example['global-1'] = random.sample(global_facts, len(example['factual-hint']))
        example['global-2'] = random.sample(global_facts, 2*len(example['factual-hint']))
        example['local-1'] = random.sample(local_facts[dataset_name], len(example['factual-hint']))
        example['local-2'] = random.sample(local_facts[dataset_name], 2*len(example['factual-hint']))
    for data in datas:
        data['global-1'] = random.sample(global_facts, len(data['factual-hint']))
        data['global-2'] = random.sample(global_facts, 2*len(data['factual-hint']))
        data['local-1'] = random.sample(local_facts[dataset_name], len(data['factual-hint']))
        data['local-2'] = random.sample(local_facts[dataset_name], 2*len(data['factual-hint']))
    
    datas_w.write(json.dumps(datas, ensure_ascii=False) + '\n')
    examples_w.write(json.dumps(examples, ensure_ascii=False) + '\n')