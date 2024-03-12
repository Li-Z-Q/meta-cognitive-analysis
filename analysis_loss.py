import json
import os 
import pandas
import numpy as np
import copy

result = {
    "model_name": [
                    # "llama-13b", "llama-30b", "llama-65b",
                    "llama-7b", "llama-13b", "llama-30b", "llama-65b",
                    "vicuna-7b-v1.3", "vicuna-13b-v1.3", "vicuna-33b-v1.3", 
                    "llama-2-7b", "llama-2-13b", "llama-2-70b", 
                    "llama-2-7b-chat", "llama-2-13b-chat", "llama-2-70b-chat",
                    "vicuna-7b-v1.5", "vicuna-13b-v1.5", 
                    "vicuna-7b-v1.5-16k", "vicuna-13b-v1.5-16k", 
                    "codellama-7b-instruct", "codellama-13b-instruct", "codellama-34b-instruct", 
                    "falcon-7b", "falcon-7b-instruct", 
                    "falcon-40b", "falcon-40b-instruct"
                ],
    "dataset_name": [
        # "gsm8k", "csqa", "truthfulqa", 
        # "csqa", "truthfulqa", 
        "arceasy", "arcchallenge", "math1", "math2", "math3", 
        "mmluhuman", "mmluother", "mmlusocial", "mmlustem"
    ], 
    "hint_type": ["procedural", "factual", "understanding"] # , "factual_hint_noise", "procedural_factual_hint_noise"
}

result["loss"] = [[[-1. for _ in range(len(result["model_name"]))] for _ in range(len(result["dataset_name"]))] for _ in range(len(result["hint_type"]))] # 3*12*20

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

            datas = [json.loads(line) for line in open(f'outputs/loss/{model_name}_{dataset_name}_{hint_type}.jsonl', 'r', encoding='utf-8').readlines()]
            assert len(datas) == 100
            
            loss = 0
            for data in datas: 
                try:
                    assert data['model_output'] > 0   
                    loss += data['model_output']
                except:
                    to_do_list.append(f'{hint_type} {dataset_name} {model_name} {data["id"]}')
                    
            print('total:', len(datas))
            result["loss"][h][d][m] = loss / len(datas)
                        
print("------------------------------------")
print("------------------------------------")
print("to do")
to_do_list = sorted(to_do_list)
for to_do in to_do_list:
    print(to_do)

json.dump(result, open(f'outputs/loss_result.json', 'w', encoding='utf-8'), ensure_ascii=False)

dir_path = 'figs/loss_result'
show_list = ["loss"]

for d in show_list:
    r = np.array(result[d])
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
            df = pandas.DataFrame(np.around(temp, decimals=3), columns=columns, index=index)
            df.style.set_properties(**{'width': '120px'})

            import os
            if not os.path.exists(f"{dir_path}/{view}_{title}"):
                os.makedirs(f"{dir_path}/{view}_{title}")

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