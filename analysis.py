import json
import os 
import pandas
import numpy as np
import copy

result = {
    "model_name": [
                    # "gpt3.5",
                    # "llama-7b", "llama-13b", "llama-30b", "llama-65b",
                    # "vicuna-7b-v1.3", "vicuna-13b-v1.3", "vicuna-33b-v1.3", 
                    # "llama-2-7b", "llama-2-13b", "llama-2-70b", 
                    # "llama-2-7b-chat", "llama-2-13b-chat", "llama-2-70b-chat",
                    # "vicuna-7b-v1.5", "vicuna-13b-v1.5", 
                    # "vicuna-7b-v1.5-16k", "vicuna-13b-v1.5-16k", 
                    # "codellama-7b-instruct", "codellama-13b-instruct", "codellama-34b-instruct",
                    "baichuan-7b-00220", "baichuan-7b-00440", "baichuan-7b-00660", "baichuan-7b-00880", "baichuan-7b-01100", "baichuan-7b-01320", "baichuan-7b-01540", "baichuan-7b-01760", "baichuan-7b-01980", "baichuan-7b-02200", "baichuan-7b-02420"
                ],
    "dataset_name": [
        "multiarith", "gsm8k",
        "csqa", "truthfulqa", 
        "arceasy", "arcchallenge", 
        "math1", "math2", "math3", 
        "mmluhuman", "mmluother", "mmlusocial", "mmlustem"
    ], 
    "hint_type": [
        "procedural_hint", 
        "factual_hint_local_2", "procedural_factual_hint_noise_local_2", 
        # "factual_hint_local_mix2", "procedural_factual_hint_noise_local_mix2", 
        # "factual_hint", "procedural_factual_hint", 
        # "factual_hint_local_1", "procedural_factual_hint_noise_local_1", 
        # "factual_hint_local_mix", "procedural_factual_hint_noise_local_mix", 
        # "factual_hint_global_1", "procedural_factual_hint_noise_global_1",
        # "factual_hint_global_mix", "procedural_factual_hint_noise_global_mix",
    ]
}

dir_path = 'figs_baichuan_local_2'

result["after"] = [[[-1. for _ in range(len(result["model_name"]))] for _ in range(len(result["dataset_name"]))] for _ in range(len(result["hint_type"]))] # 3*12*20
result["before"] = copy.deepcopy(result["after"])
result['positive'] = copy.deepcopy(result["after"])
result['negative'] = copy.deepcopy(result["after"])
# result["absolute"] = copy.deepcopy(result["after"])
# result["relative"] = copy.deepcopy(result["after"])
# result["fake_absolute"] = copy.deepcopy(result["after"])
# result["fake_relative"] = copy.deepcopy(result["after"])

result["colors"] = [
            'grey', "orange", "lime", "cornflowerblue", 
            "maroon", "gold", "darkgreen", 
            "khaki", "turquoise",
            "indianred", "bisque",
            "lightcoral", "darkorange",
            "lightgreen", "mediumseagreen", 
            "lightblue", "deepskyblue", "steelblue", 
            "plum", "violet", 
            "pink", "hotpink"
        ][:len(result["model_name"])]

to_do_list = []
for m, model_name in enumerate(result["model_name"]):
    for d, dataset_name in enumerate(result['dataset_name']):
        for h, hint_type in enumerate(result['hint_type']):
            print()
            print(hint_type, dataset_name, model_name)
            
            if hint_type == "factual_hint_local_mix":
                if dataset_name in ["gsm8k", "math1", "math2", "math3", "multiarith"]:
                    hint_type = "factual_hint_local_1"
                else:
                    hint_type = "factual_hint"
            elif hint_type == "procedural_factual_hint_noise_local_mix":
                if dataset_name in ["gsm8k", "math1", "math2", "math3", "multiarith"]:
                    hint_type = "procedural_factual_hint_noise_local_1"
                else:
                    hint_type = "procedural_factual_hint"
                    
            elif hint_type == "factual_hint_local_mix2":
                if dataset_name in ["gsm8k", "math1", "math2", "math3", "multiarith"]:
                    hint_type = "factual_hint_local_2"
                else:
                    hint_type = "factual_hint"
            elif hint_type == "procedural_factual_hint_noise_local_mix2":
                if dataset_name in ["gsm8k", "math1", "math2", "math3", "multiarith"]:
                    hint_type = "procedural_factual_hint_noise_local_2"
                else:
                    hint_type = "procedural_factual_hint"
                    
            elif hint_type == "factual_hint_global_mix":
                if dataset_name in ["gsm8k", "math1", "math2", "math3", "multiarith"]:
                    hint_type = "factual_hint_global_1"
                else:
                    hint_type = "factual_hint"
            elif hint_type == "procedural_factual_hint_noise_global_mix":
                if dataset_name in ["gsm8k", "math1", "math2", "math3", "multiarith"]:
                    hint_type = "procedural_factual_hint_noise_global_1"
                else:
                    hint_type = "procedural_factual_hint"

            datas = [json.loads(line) for line in open(f'outputs/annotations/{model_name}_{dataset_name}_with_{hint_type}_ann.jsonl', 'r', encoding='utf-8').readlines()]
            no_datas = [json.loads(line) for line in open(f'outputs/annotations/{model_name}_{dataset_name}_with_no_hint_ann.jsonl', 'r', encoding='utf-8').readlines()]
            assert len(datas) == 100
            assert len(no_datas) == len(datas)
            
            positive = 0
            negative = 0
            no_hint_ann = 0
            with_hint_ann = 0

            for data, no_data in zip(datas, no_datas):    
                    
                no_hint_ann += no_data['model_output_ann']
                with_hint_ann += data['model_output_ann']

                if no_data['model_output_ann'] == 0 and data['model_output_ann'] == 1:
                    positive += 1
                elif no_data['model_output_ann'] == 1 and data['model_output_ann'] == 0:
                    negative += 1
                    
            print('total:', len(datas))
            assert len(datas) == len(no_datas) == 100

            # print(no_hint_ann, round(no_hint_ann/len(datas), 2))
            # print(with_hint_ann, round(with_hint_ann/len(datas), 2))

            # print("w/o hint get error and w/ hint correct")
            # print(increase, round(increase/len(datas), 2))
            
            # input('press enter to continue')
                        
            result["after"][h][d][m] = with_hint_ann / len(datas)
            result["before"][h][d][m] = no_hint_ann / len(datas)
            result["positive"][h][d][m] = positive / len(datas)
            result["negative"][h][d][m] = negative / len(datas)
                        
print("------------------------------------")
print("------------------------------------")
print("to do")
to_do_list = sorted(to_do_list)
for to_do in to_do_list:
    print(to_do)


after = np.array(result["after"])
before = np.array(result["before"])
positive = np.array(result["positive"])
negative = np.array(result["negative"])
# fake_after = before + positive
result["absoluteq"] = copy.deepcopy(after)
result['absoluteq'][-1] = 1 - after[-1]
result["absoluteq"][0] = after[-1] - after[1]
result["absoluteq"][1] = after[-1] - after[0]
result["absoluteq"] = result["absoluteq"].tolist()

result["absolute"] = copy.deepcopy(after)
# result['absolute'][-1] = 1 - after[-1]
result["absolute"][0] = after[0] - before[0]
result["absolute"][1] = after[1] - before[1]
result["absolute"][2] = after[2] - before[2]
result["absolute"] = result["absolute"].tolist()

result['fake_absolute'] = copy.deepcopy(after)
result['fake_absolute'] = positive
# result['fake_absolute'][-1] = 1 - fake_after[-1]
# result['fake_absolute'][0] = fake_after[0] - before[0]
# result['fake_absolute'][1] = fake_after[1] - before[1]
# result['fake_absolute'] = result['fake_absolute'] * negative
result['fake_absolute'] = result['fake_absolute'].tolist()

json.dump(result, open(f'{dir_path}/result.json', 'w', encoding='utf-8'), ensure_ascii=False)
show_list = ["absolute", "after", "before", "positive", "negative", "absoluteq", "fake_absolute"]

for d in show_list:
    r = np.array(result[d])
    r[np.where(r==-1)] = np.nan
    for view in ["hint_type", "dataset_name", "model_name"]:
        for i, title in enumerate(result[view]):

            temp_choices = ["model_name", "dataset_name", "hint_type"]
            temp_choices.remove(view)
            index = result[temp_choices[0]] + ['average']
            columns = result[temp_choices[1]] + ['average']
            
            if view == "hint_type":
                temp = np.zeros((r.shape[1]+1, r.shape[2]+1))
                temp[:-1, :-1] = r[i, :, :]
                temp[-1, :-1] = np.nanmean(r[i, :, :], axis=0)
                temp[:-1, -1] = np.nanmean(r[i, :, :], axis=1)
            elif view == "dataset_name":
                temp = np.zeros((r.shape[0]+1, r.shape[2]+1))
                temp[:-1, :-1] = r[:, i, :]
                temp[-1, :-1] = np.nanmean(r[:, i, :], axis=0)
                temp[:-1, -1] = np.nanmean(r[:, i, :], axis=1)
            elif view == "model_name":
                temp = np.zeros((r.shape[0]+1, r.shape[1]+1))
                temp[:-1, :-1] = r[:, :, i]
                temp[-1, :-1] = np.nanmean(r[:, :, i], axis=0)
                temp[:-1, -1] = np.nanmean(r[:, :, i], axis=1)
                
            temp = temp.T
            # temp[-1, -1] show how many is lower than 0
            temp[-1, -1] = np.sum(temp[:-1, :-1] < 0) + 0.01*np.sum(1-np.isnan(temp[:-1, :-1]))
            df = pandas.DataFrame(np.around(temp, decimals=3), columns=columns, index=index)
            df.style.set_properties(**{'width': '120px'})

            import os
            if not os.path.exists(f"{dir_path}/{view}_{title}"):
                os.makedirs(f"{dir_path}/{view}_{title}")

            # if d not in ["before", "after"]:

            if not os.path.exists(f'{dir_path}/{view}_{title}/{view}_{title}_{d}'):
                os.makedirs(f'{dir_path}/{view}_{title}/{view}_{title}_{d}')
            df.to_csv(f"{dir_path}/{view}_{title}/{view}_{title}_{d}/{view}_{title}_{d}.csv", encoding='utf-8-sig')

            i_l = [[-99 for _ in range(len(columns)-1)] for _ in range(len(index))]
            for j in range(len(index)):
                temp_i = list(temp[j, :-1])
                temp_i.sort(reverse=True)
                for k in range(len(columns)-1):
                    if not np.isnan(temp[j, k]):
                        i_l[j][k] = temp_i.index(temp[j, k])+1
                        if temp[j, k] < 0:
                            i_l[j][k] *= -1
            i_l = np.array(i_l)
            dfi = pandas.DataFrame(i_l, columns=columns[:-1], index=index[:])
            dfi.style.set_properties(**{'width': '120px'})
            dfi.to_csv(f"{dir_path}/{view}_{title}/{view}_{title}_{d}/{view}_{title}_{d}_index_order.csv", encoding='utf-8-sig')
            
            c_l = [[-99 for _ in range(len(columns))] for _ in range(len(index)-1)]
            for j in range(len(columns)):
                temp_c = list(temp[:-1, j])
                temp_c.sort(reverse=True)
                for k in range(len(index)-1):
                    if not np.isnan(temp[k, j]):
                        c_l[k][j] = temp_c.index(temp[k, j])+1    
                        if temp[k, j] < 0:
                            c_l[k][j] *= -1
            c_l = np.array(c_l)
            dfc = pandas.DataFrame(c_l, columns=columns[:], index=index[:-1])
            dfc.style.set_properties(**{'width': '120px'})
            dfc.to_csv(f"{dir_path}/{view}_{title}/{view}_{title}_{d}/{view}_{title}_{d}_column_order.csv", encoding='utf-8-sig')     
                
            # else:
            #     df.to_csv(f"{dir_path}/{view}_{title}/{view}_{title}_{d}.csv", encoding='utf-8-sig')