# -*- coding: utf-8 -*-
import json
import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import pandas
import os
# from analysis import show_list
os.system("clear")

def do_pca(matrix):  # matrix is n samples * m features
    print(matrix)
    print(matrix.shape)
    pca = PCA(n_components=12) #降到 2 维
    pca.fit(matrix)
    
    result = pca.transform(matrix) # 降维后的结果
    
    print(np.round(result, 3))
    print(result.shape)
    
    print(pca.explained_variance_ratio_) # 降维后的各主成分的方差值占总方差值的比例，即方差贡献率
    # array([0.63506778, 0.339022  ])
    # print(pca.explained_variance_) # 降维后的各主成分的方差值
    # array([306.29319053, 163.51030959])
    
    # inverse = pca.inverse_transform(result[:, :]) # 将降维后的数据转换成原始数据
    print(pca.components_.shape)
    print(pca.mean_.shape)
    inverse = np.dot(result[:, 1:], pca.components_[1:, :]) + pca.mean_
    print(np.round(inverse, 3))
    print(inverse.shape)

    return result, inverse # n samples * m features

def my_plot(datas, xs, xs_id, model_names, colors):
    
    legend = ["p", "f"]
    
    plt.figure(figsize=(16, 6))

    if xs == None:
        xs = [[n for n in model_names]]
    
    flag = 0
    for x in xs:
        try:
            assert all([i in model_names for i in x])
        except:
            print(x)
            raise ValueError("x not in model_names")
        
        flag += 1
        x_idx = [model_names.index(i) for i in x]

        for l in range(datas.shape[0]):
            y = datas[l, x_idx]
            if flag == len(xs):
                plt.plot(x, y, marker='o', markersize=3, color=colors[l], label=legend[l], linewidth=1.5)
            else:
                plt.plot(x, y, marker='o', markersize=3, color=colors[l], linewidth=1.5)
            plt.xticks(rotation=15) # model_name is too long
               
    plt.grid(linewidth=0.5, linestyle='--', color='gray', alpha=0.5)
    # plt.title(f'{title}')  
    # plt.xlabel('time') 
    # plt.ylabel('delta') 
    num1 = 0
    num2 = 0
    num3 = 3
    num4 = 0
    plt.legend(bbox_to_anchor=(1.01, num2), loc=num3, borderaxespad=num4)
    # plt.show()  
    
    plt.savefig(f'figs/pca-{show}-{pre}{xs_id}.svg')
    plt.close()


if __name__ == "__main__":
    pre = ""
    results = json.load(open(f'figs/result.json', 'r', encoding='utf-8'))
    data_names = results['dataset_name']
    model_names = results['model_name']
    colors = results['colors']
    
    # show = 'loss'
    show = 'absolute'
    print(np.array(results[show]).shape)    
    
    result0, inverse0 = do_pca(np.array(results[show])[0].T) # n_samples * d_diminsion
    result1, inverse1 = do_pca(np.array(results[show])[1].T) # n_samples * d_diminsion
    
    B = np.zeros((2, np.array(results[show]).shape[2])) # 2 * 20
    B[0, :] = np.linalg.norm(inverse0.T, axis=0)
    B[1, :] = np.linalg.norm(inverse1.T, axis=0)
    # B[0, :] = result0[:, 1]
    # B[1, :] = result1[:, 1]
    # B[2, :] = np.mean(np.array(results[show][2]), axis=0)
    # A = np.zeros((3, np.array(results[show]).shape[1]))
    # A[0, :] = np.mean(np.array(results[show][0]), axis=1)
    # A[1, :] = np.mean(np.array(results[show][1]), axis=1)
    # A[2, :] = np.mean(np.array(results[show][2]), axis=1)
            
    xs_id = '-model'        
    xs = None
    my_plot(datas=B, xs=xs, xs_id=xs_id, model_names=model_names, colors=colors)

    if 1 == 1: # no flacon
        xs_id = "-scale" # model scale
        xs = [  
                # ["llama-13b", "llama-30b", "llama-65b"],
                ["llama-7b", "llama-13b", "llama-30b", "llama-65b"],
                ["vicuna-7b-v1.3", "vicuna-13b-v1.3", "vicuna-33b-v1.3"],
                ["llama-2-7b", "llama-2-13b", "llama-2-70b"],
                ["llama-2-7b-chat", "llama-2-13b-chat", "llama-2-70b-chat"],
                ["vicuna-7b-v1.5", "vicuna-13b-v1.5"],
                ["vicuna-7b-v1.5-16k", "vicuna-13b-v1.5-16k"], 
                ["codellama-7b-instruct", "codellama-13b-instruct", "codellama-34b-instruct"]]
        my_plot(datas=B, xs=xs, xs_id=xs_id, model_names=model_names, colors=colors)
            
        xs_id = "-sft" # SFT
        xs = [  
                ["llama-7b", "vicuna-7b-v1.3"], 
                ["llama-13b", "vicuna-13b-v1.3"], 
                ["llama-30b", "vicuna-33b-v1.3"], 
                ["llama-2-7b", "vicuna-7b-v1.5"],
                ["llama-2-13b", "vicuna-13b-v1.5"]]
        my_plot(datas=B, xs=xs, xs_id=xs_id, model_names=model_names, colors=colors)
            
        xs_id = "-sftplus" # SFT + RLHF/code
        xs = [  ["llama-2-7b", "vicuna-7b-v1.5", "llama-2-7b-chat", "codellama-7b-instruct"], 
                ["llama-2-13b", "vicuna-13b-v1.5", "llama-2-13b-chat", "codellama-13b-instruct"]]
        my_plot(datas=B, xs=xs, xs_id=xs_id, model_names=model_names, colors=colors)
                            
        xs_id = '-pretrain' # pretrain
        xs = [  
                ["llama-7b", "llama-2-7b"], 
                ["llama-13b", "llama-2-13b"],
                ["llama-65b", "llama-2-70b"],
                ["vicuna-7b-v1.3", "vicuna-7b-v1.5"],
                ["vicuna-13b-v1.3", "vicuna-13b-v1.5"]]
        my_plot(datas=B, xs=xs, xs_id=xs_id, model_names=model_names, colors=colors)
        
        xs_id = '-long'
        xs = [  ["vicuna-7b-v1.5", "vicuna-7b-v1.5-16k"], 
                ["vicuna-13b-v1.5", "vicuna-13b-v1.5-16k"]]
        my_plot(datas=B, xs=xs, xs_id=xs_id, model_names=model_names, colors=colors)

        # xs_id = '-data'
        # xs = None
        # my_plot(datas=A, xs=xs, xs_id=xs_id, model_names=data_names, colors=colors)
    else:
        xs_id = "-scale" # model scale
        xs = [  
                # ["llama-13b", "llama-30b", "llama-65b"],
                ["llama-7b", "llama-13b", "llama-30b", "llama-65b"],
                ["vicuna-7b-v1.3", "vicuna-13b-v1.3", "vicuna-33b-v1.3"],
                ["llama-2-7b", "llama-2-13b", "llama-2-70b"],
                ["llama-2-7b-chat", "llama-2-13b-chat", "llama-2-70b-chat"],
                ["vicuna-7b-v1.5", "vicuna-13b-v1.5"],
                ["vicuna-7b-v1.5-16k", "vicuna-13b-v1.5-16k"], 
                ["codellama-7b-instruct", "codellama-13b-instruct", "codellama-34b-instruct"], 
                ['falcon-7b', 'falcon-40b'],
                ['falcon-7b-instruct', 'falcon-40b-instruct']]
        my_plot(datas=B, xs=xs, xs_id=xs_id, model_names=model_names, colors=colors)
            
        xs_id = "-sft" # SFT
        xs = [  
                ["llama-7b", "vicuna-7b-v1.3"], 
                ["llama-13b", "vicuna-13b-v1.3"], 
                ["llama-30b", "vicuna-33b-v1.3"], 
                ["llama-2-7b", "vicuna-7b-v1.5"],
                ["llama-2-13b", "vicuna-13b-v1.5"],
                ['falcon-7b', 'falcon-7b-instruct'], 
                ['falcon-40b', 'falcon-40b-instruct']]
        my_plot(datas=B, xs=xs, xs_id=xs_id, model_names=model_names, colors=colors)
            
        xs_id = "-sftplus" # SFT + RLHF/code
        xs = [  ["llama-2-7b", "vicuna-7b-v1.5", "llama-2-7b-chat", "codellama-7b-instruct"], 
                ["llama-2-13b", "vicuna-13b-v1.5", "llama-2-13b-chat", "codellama-13b-instruct"]]
        my_plot(datas=B, xs=xs, xs_id=xs_id, model_names=model_names, colors=colors)
                            
        xs_id = '-pretrain' # pretrain
        xs = [  
                ["falcon-7b", "llama-7b", "llama-2-7b"], 
                ["llama-13b", "llama-2-13b"], 
                ["falcon-40b", "llama-30b"],
                ["llama-65b", "llama-2-70b"],
                ["vicuna-7b-v1.3", "vicuna-7b-v1.5"],
                ["vicuna-13b-v1.3", "vicuna-13b-v1.5"]]
        my_plot(datas=B, xs=xs, xs_id=xs_id, model_names=model_names, colors=colors)
        
        xs_id = '-long'
        xs = [  ["vicuna-7b-v1.5", "vicuna-7b-v1.5-16k"], 
                ["vicuna-13b-v1.5", "vicuna-13b-v1.5-16k"]]
        my_plot(datas=B, xs=xs, xs_id=xs_id, model_names=model_names, colors=colors)

        # xs_id = '-data'
        # xs = None
        # my_plot(datas=A, xs=xs, xs_id=xs_id, model_names=data_names, colors=colors)
        
