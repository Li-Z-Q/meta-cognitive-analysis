import time
import requests
import json
import random
random.seed(42)
from utils.use_my_api import get_loss

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--url_id", type=int, default=140)
    parser.add_argument("--model_name", type=str, default="llama-7b")
    parser.add_argument("--dataset_name", type=str, default="csqa")
    args = parser.parse_args()
    
    url = "http://124.16.138.{}".format(args.url_id)
    model_name = args.model_name
    dataset_name = args.dataset_name
    
    datas = json.load(open(f"datas/datas_with_hint/{dataset_name}_final.json", encoding="utf-8"))
    datas = datas[:100]
    print('len datas: ', len(datas))
    assert len(datas) == 100
    
    save_path = f'outputs/loss/{model_name}_{dataset_name}_factual.jsonl'
    save_file = open(save_path, 'a')
    already_datas_ids = [json.loads(l)["id"] for l in open(save_path, 'r').readlines()]
    datas = [data for data in datas if data["id"] not in already_datas_ids]
    print("len already_datas: ", len(already_datas_ids))
    print('len datas after filter already: ', len(datas))
        
    for data in datas:
        
        facts = data['factual-hint']
        random.shuffle(facts)
                
        instruction = "Here are some facts:\n"
        text = instruction + '\n'.join(facts)
        
        data["model_output"] = get_loss(text, instruction, url, model_name)
        
        save_file.write(json.dumps(data, ensure_ascii=False) + '\n')
        save_file.flush()
            
    save_file.close()        

        
