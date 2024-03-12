import time
import requests
import json
import random
random.seed(42)
from utils.use_my_api import get_messages
from utils.use_gpt_api import make_api_request

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--url_id", type=int, default=142)
    parser.add_argument("--model_name", type=str, default="vicuna-7b-v1.3")
    parser.add_argument("--dataset_name", type=str, default="csqa")
    args = parser.parse_args()
    
    url = "http://124.16.138.{}".format(args.url_id)
    model_name = args.model_name
    dataset_name = args.dataset_name
      
    datas = json.load(open(f"datas/datas_with_hint/{dataset_name}_final.json", encoding="utf-8"))
    datas = datas[:100]
    print('len datas: ', len(datas))
    assert len(datas) == 100
    
    save_path = f'outputs/model_outputs/{model_name}_{dataset_name}_with_procedural_hint.jsonl'
    save_file = open(save_path, 'a')
    save_file_complete = open(save_path.replace('.jsonl', '') + '_complete.jsonl', 'a')
    already_datas_ids = [json.loads(l)["id"] for l in open(save_path, 'r').readlines()]
    datas = [data for data in datas if data["id"] not in already_datas_ids]
    print("len already_datas: ", len(already_datas_ids))
    print('len datas after filter already: ', len(datas))
    
    examples = json.load(open(f"datas/examples/{dataset_name}_examples.json", encoding="utf-8"))
    
    for data in datas:
        
        random.shuffle(examples)
        hint0 = '\n'.join(examples[0]["procedural-hint"])
        hint1 = '\n'.join(examples[1]["procedural-hint"])
        hint = '\n'.join(data["procedural-hint"])
        
        model_input = \
f"""Generate reasoning for question based on procedural hint.

Question:
{examples[0]["question"]}
Procedural hint:
{hint0}
Reasoning:
{examples[0]["reasoning"]}

Question:
{examples[1]["question"]}
Procedural hint:
{hint1}
Reasoning:
{examples[1]["reasoning"]}

Question:
{data["question"]}
Procedural hint:
{hint}
Reasoning:"""
        
        if model_name == "gpt3.5":
            data["model_output"] = make_api_request(model="gpt-3.5-turbo", prompt=model_input, max_tokens=512, temperature=0)
        else:
            data["model_output"] = get_messages(model_input, url, model_name)
        
        save_file.write(json.dumps(data, ensure_ascii=False) + '\n')
        save_file.flush()
        
        data['model_input'] = model_input
        save_file_complete.write(json.dumps(data, ensure_ascii=False) + '\n')
        save_file_complete.flush()
        
    save_file.close()
    save_file_complete.close()
        


    
        
