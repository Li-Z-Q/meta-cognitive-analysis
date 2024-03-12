import json
import os
from colorama import init, Fore, Back, Style
init(autoreset=True)
import transformers

def IsFloatNum(str):
    s=str.split('.')
    if len(s)>2:
        return False
    else:
        for si in s:
            if not si.isdigit():
                return False
        return True

no_output_list = {}
for dataset_name in [
    "multiarith", "gsm8k", 
    "csqa", "truthfulqa", 
    "arceasy", "arcchallenge", 
    "math1", "math2", "math3", 
    "mmluhuman", "mmluother", "mmlusocial", "mmlustem"
    ]:
    for hint_type in [
        "no_hint",
        "procedural_hint", 
        "factual_hint_local_2", "procedural_factual_hint_noise_local_2", 
        # "factual_hint", "procedural_factual_hint", 
        # "factual_hint_global_1", "procedural_factual_hint_noise_global_1",
        # "factual_hint_local_1", "procedural_factual_hint_noise_local_1", 
    ]:  
        for model_name in [
            # "gpt3.5",
            # "llama-7b", "llama-13b", "llama-30b", "llama-65b",
            # "vicuna-7b-v1.3", "vicuna-13b-v1.3", "vicuna-33b-v1.3", 
            # "llama-2-7b", "llama-2-13b", "llama-2-70b", 
            # "llama-2-7b-chat", "llama-2-13b-chat", "llama-2-70b-chat",
            # "vicuna-7b-v1.5", "vicuna-13b-v1.5", 
            # "vicuna-7b-v1.5-16k", "vicuna-13b-v1.5-16k", 
            # "codellama-7b-instruct", "codellama-13b-instruct", "codellama-34b-instruct"
            "baichuan-7b-00220", "baichuan-7b-00440", "baichuan-7b-00660", "baichuan-7b-00880", "baichuan-7b-01100", "baichuan-7b-01320", "baichuan-7b-01540", "baichuan-7b-01760", "baichuan-7b-01980", "baichuan-7b-02200", "baichuan-7b-02420"
            ]:
            print('\n\n')
            print(f"model_name: {model_name}, dataset_name: {dataset_name}, hint_type: {hint_type}")

            datas = [json.loads(line) for line in open(f'outputs/model_outputs/{model_name}_{dataset_name}_with_{hint_type}.jsonl', 'r', encoding='utf-8')]
            print("len(datas): ", len(datas))
            try:
                assert len(datas) == 100
            except Exception as e:
                print(e)
                input("enter to continue")
            
            save_path = f'outputs/annotations/{model_name}_{dataset_name}_with_{hint_type}_ann.jsonl'
            save_file = open(save_path, 'w', encoding='utf-8')
            already_datas_ids = [json.loads(l)["id"] for l in open(save_path, 'r').readlines()]
            datas = [data for data in datas if data["id"] not in already_datas_ids]
            print("len already_datas: ", len(already_datas_ids))
            print('len datas after filter already: ', len(datas))
            # input("enter to continue")

            for i, data in enumerate(datas):
                
                try:
                    assert data['model_output'] not in ['', '\n', None]
                except Exception as e:
                    k = f"{model_name}   {dataset_name}_{hint_type}"
                    if k not in list(no_output_list.keys()):
                        no_output_list[k] = [data]
                    else:
                        no_output_list[k].append(data)
                    data['model_output'] = 'None'
                
                data['model_output_answer'] = data['model_output'].split('\nQuestion:')[0].strip()
                if "Therefore, the answer is" in data['model_output_answer']:
                    data['model_output_answer'] = data['model_output_answer'].split('Therefore, the answer is')[1].strip().strip('.')
                if data['model_output_answer'] == '':
                    data['model_output_answer'] = 'None'
                
                if 1:
                    model_output_ann = 0
                    if data['model_output_answer'] == data['answer']:
                        model_output_ann = 1
                    if dataset_name in ["gsm8k", "math1", "math2", "math3", "multiarith"]:
                        # if IsFloatNum(data['model_output_answer']):
                        #     model_output_ann = int(float(data['model_output_answer']) == float(data['answer']))
                        temp = data['model_output_answer'].split(' ')
                        if len(temp) == 1:
                            temp_s = temp[0]
                            temp_s = "".join(filter(str.isdigit, temp_s))
                            model_output_ann = int(temp_s == data['answer'])
                        else:
                            for t in temp:
                                if len(t) > 0 and not t[0].isalpha():
                                    temp_s = t
                                    break
                            temp_s = "".join(filter(str.isdigit, temp_s))
                            model_output_ann = int(temp_s == data['answer'])
                                    
                    if dataset_name not in ["gsm8k", "math1", "math2", "math3", "multiarith"]:
                        if data['model_output_answer'][0] == data['answer'][0]:
                            model_output_ann = 1
                        if data['model_output_answer'].split('.')[-1].strip() == data['answer'].split('.')[-1].strip():
                            model_output_ann = 1
                
                while 0:
                    
                    if data['model_output_answer'] == data['answer']:
                        model_output_ann = 1
                        break
                    else:
                        if dataset_name in ["gsm8k", "multiarith"]:
                            temp = data['model_output_answer'].replace(",", "")
                            if IsFloatNum(temp) and IsFloatNum(data['answer']):
                                model_output_ann = int(float(temp) == float(data['answer']))
                                break
                            if IsFloatNum(temp.split(' ')[0]):
                                model_output_ann = int(float(temp.split(' ')[0]) == float(data['answer']))
                                break
                        if dataset_name in ["coin", "strategy"]:
                            if data['model_output_answer'] in ['yes', 'no']:
                                model_output_ann = int(data['model_output_answer'] == data['answer'])
                                break
                        if dataset_name in ['strategy']:
                            if data['model_output_answer'] == 'unknown':
                                model_output_ann = 0
                                break
                            temp = data['model_output_answer'].split('\nQuestion:')[0].strip()
                            if 'the answer is' in temp:
                                temp_ = temp.split('the answer is')[-1].strip().strip('.')
                                if temp_ in ['yes', 'no']:
                                    model_output_ann = int(temp_ == data['answer'])
                                    break
                        if dataset_name in ['tracking3', 'tracking5', 'dateu']:
                            if data['model_output_answer'] in data['question'].lower():
                                model_output_ann = int(data['model_output_answer'] == data['answer'].lower())
                                break
                        if dataset_name in ['dateu']:
                            temp = data['model_output_answer'].split(' ')[-1].strip()
                            if len(temp.split('/')) == 3:
                                if temp.split('/')[0].isdigit() and temp.split('/')[1].isdigit() and temp.split('/')[2].isdigit():
                                    model_output_ann = int(temp == data['answer'].split(' ')[-1].strip())
                                    break
                        if dataset_name in ['tracking3', 'tracking5']:
                            if data['model_output_answer'].split(' ')[-1] in ['ball', 'present']:
                                if data['model_output_answer'].split(' ')[0] in ['orange', 'blue', 'green', 'red', 'white', 'black']:
                                    model_output_ann = int(data['model_output_answer'] == data['answer'])
                                    break
                        if dataset_name in ['letter']:
                            model_output_ann = int(data['model_output_answer'] == data['answer'])
                            break
                        if dataset_name in ['dateu', 'csqa']:
                            if data['model_output_answer'].split('.')[-1].strip() in data['question']:
                                model_output_ann = int(data['model_output_answer'].split('.')[-1].strip() == data['answer'].split('.')[-1].strip())
                                break 
                        if dataset_name in ['csqa']:
                            if data['model_output_answer'].lower() == data['answer'].lower():
                                model_output_ann = 1
                                break
                            temp = data['model_output_answer'].split('\nQuestion')[0].strip().split('answer is')[-1].strip('.').strip()
                            if temp.split(' ')[-1].strip() in data['question']:
                                model_output_ann = int(temp.split(' ')[-1].strip() == data['answer'].split(' ')[-1].strip())
                                break
                    os.system('clear')
                    print(data['id'])
                    print(data['question'])
                    print()
                            
                    # print(Fore.GREEN + f"model_output:\n" + data['model_output'])
                    print(Fore.RED + f"model_output_answer:\n" + data['model_output_answer'])
                    print(Fore.BLUE + "answer:\n" + data['answer'])
                    model_output_ann = input(Fore.WHITE + f"model_output_ann:")

                    if model_output_ann == 'check':
                        print(Fore.GREEN + f"model_output:\n" + data['model_output'])
                        input("press enter to continue")
                        continue
                    
                    if model_output_ann not in ["0", "1", 0, 1]:
                        print('not in ["0", "1"]')
                        input("press enter to continue")
                        continue
                    
                    re_ann = input("re_ann ? input y:")
                    if re_ann != 'y':
                        break
                    
                data['model_output_ann'] = int(model_output_ann)
                    
                save_file.write(json.dumps(data, ensure_ascii=False) + '\n')
                save_file.flush()
            save_file.close()

print('===============================================')
for name in list(no_output_list.keys()):
    print(name, len(no_output_list[name]))