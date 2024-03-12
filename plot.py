# -*- coding: utf-8 -*-
import json
import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt
import os
# from analysis import show_list
os.system("clear")
import seaborn as sns
import pandas as pd
from sklearn.preprocessing import normalize
from matplotlib import colorbar

def my_plot(datas, xs, group_name, model_names, colors, datas_before=None, datas_after=None):
    if xs == None:
        xs = [[n for n in model_names]]

    i = 0
    x_widths = [[] for _ in range(len(xs))]
    for x, x_w in zip(xs, x_widths):
        for _ in x:
            x_w.append(i)
            i += 1
        # i += 2

    legend = ["p", "f", 'o']
    
    plt.figure(figsize=(16, 6))

    
    flag = 0
    for x, x_w in zip(xs, x_widths):
        try:
            assert all([i in model_names for i in x])
        except:
            print(x)
            raise ValueError("x not in model_names")
        
        flag += 1
        for l in range(datas.shape[0]): # datas.shape is 3*20
            y = datas[l, [model_names.index(i) for i in x]]
            if flag == len(xs):
                plt.plot(x, y, marker='o', markersize=3, color=colors[l], label=legend[l], linewidth=1.5)
            else:
                plt.plot(x, y, marker='o', markersize=3, color=colors[l], linewidth=1.5)
            
            x_w_l = []
            for i in x_w:
                if l == 0:
                    x_w_l.append(i-0.1)
                if l == 1:
                    x_w_l.append(i)
                if l == 2:
                    x_w_l.append(i+0.1)
            
            plt.bar(x_w_l, 
                    datas_before[l, [model_names.index(i) for i in x]], lw=0.5, fc="grey", width=0.1, alpha=0.5)
            plt.bar(x_w_l, 
                    datas_after[l, [model_names.index(i) for i in x]] - datas_before[l, [model_names.index(i) for i in x]], 
                    lw=0.5, fc=colors[l], width=0.1, alpha=0.5,
                    bottom=datas_before[l, [model_names.index(i) for i in x]])

            plt.xticks(rotation=15) # model_name is too long
               
    plt.grid(linewidth=0.5, linestyle='--', color='gray', alpha=0.5)
    # plt.title(f'{title}')  
    # plt.xlabel('time') 
    plt.ylabel('acc') 
    num1 = 0
    num2 = 0
    num3 = 3
    num4 = 0
    plt.legend(bbox_to_anchor=(1.01, num2), loc=num3, borderaxespad=num4)
    # plt.show()  
    
    plt.savefig(f'{dir_path}/{show}-{pre}{group_name}.svg')
    plt.close()

def plot_heatmap(data, data_names, model_names, title):
    plt.figure(figsize=(16, 8))
    # data = data * 100
    # data = data.astype(int)
    data = pd.DataFrame(data, index=data_names, columns=model_names)
    cmap = sns.heatmap(data, linewidths=0.8, annot=True, fmt=".2f", cmap="RdBu_r")
    # plt.xlabel("X", size=20)
    # plt.ylabel("Y", size=20,rotation=0)
    plt.title(f"{title}", size=20)
    cbar = cmap.collections[0].colorbar
    cbar.ax.tick_params(labelsize=20, labelcolor="black")
    # cbar.ax.set_ylabel(ylabel="color scale", size=20, color="red",loc="center")
    plt.xticks(rotation=15) # model_name is too long
    plt.savefig(f'{dir_path}/heatmap-{title}.svg')
    plt.close()
    print(f'{title} heat map done')

if __name__ == "__main__":
    dir_path = "figs_baichuan_local_2"
    pre = ""
    results = json.load(open(f'{dir_path}/result.json', 'r', encoding='utf-8'))
    data_names = results['dataset_name']
    model_names = results['model_name']
    
    plot_heatmap(np.array(results['before'][0]), data_names, model_names, title='before')
    plot_heatmap(np.array(results['after'][0]), data_names, model_names, title='after0')
    plot_heatmap(np.array(results['after'][1]), data_names, model_names, title='after1')
    plot_heatmap(np.array(results['after'][2]), data_names, model_names, title='after2')

    plot_heatmap(np.array(results['absolute'][0]), data_names, model_names, title='absolute0')
    plot_heatmap(normalize(np.array(results['absolute'][0]), axis=0, norm='l1'), data_names, model_names, title='absolute0_l1_axis0')
    plot_heatmap(normalize(np.array(results['absolute'][0]), axis=1, norm='l1'), data_names, model_names, title='absolute0_l1_axis1')
    plot_heatmap(normalize(np.array(results['absolute'][0]), axis=0, norm='l2'), data_names, model_names, title='absolute0_l2_axis0')
    plot_heatmap(normalize(np.array(results['absolute'][0]), axis=1, norm='l2'), data_names, model_names, title='absolute0_l2_axis1')
    plot_heatmap(normalize(np.array(results['absolute'][0]), axis=0, norm='max'), data_names, model_names, title='absolute0_max_axis0')
    plot_heatmap(normalize(np.array(results['absolute'][0]), axis=1, norm='max'), data_names, model_names, title='absolute0_max_axis1')

    plot_heatmap(np.array(results['absolute'][1]), data_names, model_names, title='absolute1')    
    plot_heatmap(normalize(np.array(results['absolute'][1]), axis=0, norm='l1'), data_names, model_names, title='absolute1_l1_axis0')
    plot_heatmap(normalize(np.array(results['absolute'][1]), axis=1, norm='l1'), data_names, model_names, title='absolute1_l1_axis1')
    plot_heatmap(normalize(np.array(results['absolute'][1]), axis=0, norm='l2'), data_names, model_names, title='absolute1_l2_axis0')
    plot_heatmap(normalize(np.array(results['absolute'][1]), axis=1, norm='l2'), data_names, model_names, title='absolute1_l2_axis1')
    plot_heatmap(normalize(np.array(results['absolute'][1]), axis=0, norm='max'), data_names, model_names, title='absolute1_max_axis0')
    plot_heatmap(normalize(np.array(results['absolute'][1]), axis=1, norm='max'), data_names, model_names, title='absolute1_max_axis1')
    
    plot_heatmap(np.array(results['absolute'][2]), data_names, model_names, title='absolute2')
    plot_heatmap(normalize(np.array(results['absolute'][2]), axis=0, norm='l1'), data_names, model_names, title='absolute2_l1_axis0')
    plot_heatmap(normalize(np.array(results['absolute'][2]), axis=1, norm='l1'), data_names, model_names, title='absolute2_l1_axis1')
    plot_heatmap(normalize(np.array(results['absolute'][2]), axis=0, norm='l2'), data_names, model_names, title='absolute2_l2_axis0')
    plot_heatmap(normalize(np.array(results['absolute'][2]), axis=1, norm='l2'), data_names, model_names, title='absolute2_l2_axis1')
    plot_heatmap(normalize(np.array(results['absolute'][2]), axis=0, norm='max'), data_names, model_names, title='absolute2_max_axis0')
    plot_heatmap(normalize(np.array(results['absolute'][2]), axis=1, norm='max'), data_names, model_names, title='absolute2_max_axis1')
    
    f_over_p = np.array(results['after'][1])-np.array(results['after'][0])
    plot_heatmap(f_over_p, data_names, model_names, title='f_over_p')
    plot_heatmap(normalize(f_over_p, axis=0, norm='l1'), data_names, model_names, title='f_over_p_l1_axis0')
    plot_heatmap(normalize(f_over_p, axis=1, norm='l1'), data_names, model_names, title='f_over_p_l1_axis1')
    plot_heatmap(normalize(f_over_p, axis=0, norm='l2'), data_names, model_names, title='f_over_p_l2_axis0')
    plot_heatmap(normalize(f_over_p, axis=1, norm='l2'), data_names, model_names, title='f_over_p_l2_axis1')
    plot_heatmap(normalize(f_over_p, axis=0, norm='max'), data_names, model_names, title='f_over_p_max_axis0')
    plot_heatmap(normalize(f_over_p, axis=1, norm='max'), data_names, model_names, title='f_over_p_max_axis1')
    
    # colors = results['colors']
    colors = ['red', 'green', 'blue']
    # show = 'loss'
    show = 'absolute'
    print(np.array(results[show]).shape)
    model_score = np.zeros((3, np.array(results[show]).shape[2]))
    model_score[0, :] = np.mean(np.array(results[show][0]), axis=0)
    model_score[1, :] = np.mean(np.array(results[show][1]), axis=0)
    model_score[2, :] = np.mean(np.array(results[show][2]), axis=0)
    # model_score[0, :] = np.linalg.norm(np.array(results[show][0]), axis=0)
    # model_score[1, :] = np.linalg.norm(np.array(results[show][1]), axis=0)
    # model_score[2, :] = np.linalg.norm(np.array(results[show][2]), axis=0)
    dataset_score = np.zeros((3, np.array(results[show]).shape[1]))
    dataset_score[0, :] = np.mean(np.array(results[show][0]), axis=1)
    dataset_score[1, :] = np.mean(np.array(results[show][1]), axis=1)
    dataset_score[2, :] = np.mean(np.array(results[show][2]), axis=1)
    # dataset_score[0, :] = np.linalg.norm(np.array(results[show][0]), axis=1)
    # dataset_score[1, :] = np.linalg.norm(np.array(results[show][1]), axis=1)
    # dataset_score[2, :] = np.linalg.norm(np.array(results[show][2]), axis=1)

    model_before = np.mean(np.array(results['before']), axis=1)
    dataset_before = np.mean(np.array(results['before']), axis=2)
    model_after = np.mean(np.array(results['after']), axis=1)
    dataset_after = np.mean(np.array(results['after']), axis=2)
    
    group_name = '-data'
    xs = None
    my_plot(datas=dataset_score, xs=xs, group_name=group_name, model_names=data_names, colors=colors, datas_before=dataset_before, datas_after=dataset_after)
    
    group_name = '-model'        
    xs = None
    my_plot(datas=model_score, xs=xs, group_name=group_name, model_names=model_names, colors=colors, datas_before=model_before, datas_after=model_after)

    # if 1 == 1: # no flacon
    #     group_name = "-scale" # model scale
    #     xs = [  
    #             # ["llama-13b", "llama-30b", "llama-65b"],
    #             ["llama-7b", "llama-13b", "llama-30b", "llama-65b"],
    #             ["vicuna-7b-v1.3", "vicuna-13b-v1.3", "vicuna-33b-v1.3"],
    #             ["llama-2-7b", "llama-2-13b", "llama-2-70b"],
    #             ["llama-2-7b-chat", "llama-2-13b-chat", "llama-2-70b-chat"],
    #             ["vicuna-7b-v1.5", "vicuna-13b-v1.5"],
    #             ["vicuna-7b-v1.5-16k", "vicuna-13b-v1.5-16k"], 
    #             ["codellama-7b-instruct", "codellama-13b-instruct", "codellama-34b-instruct"]]
    #     my_plot(datas=model_score, xs=xs, group_name=group_name, model_names=model_names, colors=colors, datas_before=model_before, datas_after=model_after)
            
    #     group_name = "-sft" # SFT
    #     xs = [  
    #             ["llama-7b", "vicuna-7b-v1.3"], 
    #             ["llama-13b", "vicuna-13b-v1.3"], 
    #             ["llama-30b", "vicuna-33b-v1.3"], 
    #             ["llama-2-7b", "vicuna-7b-v1.5", "llama-2-7b-chat", "codellama-7b-instruct"],
    #             ["llama-2-13b", "vicuna-13b-v1.5", "llama-2-13b-chat", "codellama-13b-instruct"]]
    #     my_plot(datas=model_score, xs=xs, group_name=group_name, model_names=model_names, colors=colors, datas_before=model_before, datas_after=model_after)
            
    #     # group_name = "-sftplus" # SFT + RLHF/code
    #     # xs = [  ["llama-2-7b", "vicuna-7b-v1.5", "llama-2-7b-chat", "codellama-7b-instruct"], 
    #     #         ["llama-2-13b", "vicuna-13b-v1.5", "llama-2-13b-chat", "codellama-13b-instruct"]]
    #     # my_plot(datas=model_score, xs=xs, group_name=group_name, model_names=model_names, colors=colors, datas_before=model_before, datas_after=model_after)
                            
    #     group_name = '-pretrain' # pretrain
    #     xs = [  
    #             ["llama-7b", "llama-2-7b"], 
    #             ["llama-13b", "llama-2-13b"],
    #             ["llama-65b", "llama-2-70b"],
    #             ["vicuna-7b-v1.3", "vicuna-7b-v1.5"],
    #             ["vicuna-13b-v1.3", "vicuna-13b-v1.5"]]
    #     my_plot(datas=model_score, xs=xs, group_name=group_name, model_names=model_names, colors=colors, datas_before=model_before, datas_after=model_after)
        
    #     group_name = '-long'
    #     xs = [  ["vicuna-7b-v1.5", "vicuna-7b-v1.5-16k"], 
    #             ["vicuna-13b-v1.5", "vicuna-13b-v1.5-16k"]]
    #     my_plot(datas=model_score, xs=xs, group_name=group_name, model_names=model_names, colors=colors, datas_before=model_before, datas_after=model_after)

    # else:
    #     group_name = "-scale" # model scale
    #     xs = [  
    #             # ["llama-13b", "llama-30b", "llama-65b"],
    #             ["llama-7b", "llama-13b", "llama-30b", "llama-65b"],
    #             ["vicuna-7b-v1.3", "vicuna-13b-v1.3", "vicuna-33b-v1.3"],
    #             ["llama-2-7b", "llama-2-13b", "llama-2-70b"],
    #             ["llama-2-7b-chat", "llama-2-13b-chat", "llama-2-70b-chat"],
    #             ["vicuna-7b-v1.5", "vicuna-13b-v1.5"],
    #             ["vicuna-7b-v1.5-16k", "vicuna-13b-v1.5-16k"], 
    #             ["codellama-7b-instruct", "codellama-13b-instruct", "codellama-34b-instruct"], 
    #             ['falcon-7b', 'falcon-40b'],
    #             ['falcon-7b-instruct', 'falcon-40b-instruct']]
    #     my_plot(datas=model_score, xs=xs, group_name=group_name, model_names=model_names, colors=colors)
            
    #     group_name = "-sft" # SFT
    #     xs = [  
    #             ["llama-7b", "vicuna-7b-v1.3"], 
    #             ["llama-13b", "vicuna-13b-v1.3"], 
    #             ["llama-30b", "vicuna-33b-v1.3"], 
    #             ["llama-2-7b", "vicuna-7b-v1.5", "llama-2-7b-chat", "codellama-7b-instruct"],
    #             ["llama-2-13b", "vicuna-13b-v1.5", "llama-2-13b-chat", "codellama-13b-instruct"],
    #             ['falcon-7b', 'falcon-7b-instruct'], 
    #             ['falcon-40b', 'falcon-40b-instruct']]
    #     my_plot(datas=model_score, xs=xs, group_name=group_name, model_names=model_names, colors=colors)
            
    #     # group_name = "-sftplus" # SFT + RLHF/code
    #     # xs = [  ["llama-2-7b", "vicuna-7b-v1.5", "llama-2-7b-chat", "codellama-7b-instruct"], 
    #     #         ["llama-2-13b", "vicuna-13b-v1.5", "llama-2-13b-chat", "codellama-13b-instruct"]]
    #     # my_plot(datas=model_score, xs=xs, group_name=group_name, model_names=model_names, colors=colors)
                            
    #     group_name = '-pretrain' # pretrain
    #     xs = [  
    #             ["falcon-7b", "llama-7b", "llama-2-7b"], 
    #             ["llama-13b", "llama-2-13b"], 
    #             ["falcon-40b", "llama-30b"],
    #             ["llama-65b", "llama-2-70b"],
    #             ["vicuna-7b-v1.3", "vicuna-7b-v1.5"],
    #             ["vicuna-13b-v1.3", "vicuna-13b-v1.5"]]
    #     my_plot(datas=model_score, xs=xs, group_name=group_name, model_names=model_names, colors=colors)
        
    #     group_name = '-long'
    #     xs = [  ["vicuna-7b-v1.5", "vicuna-7b-v1.5-16k"], 
    #             ["vicuna-13b-v1.5", "vicuna-13b-v1.5-16k"]]
    #     my_plot(datas=model_score, xs=xs, group_name=group_name, model_names=model_names, colors=colors)

    #     group_name = '-data'
    #     xs = None
    #     my_plot(datas=dataset_score, xs=xs, group_name=group_name, model_names=data_names, colors=colors)
        
