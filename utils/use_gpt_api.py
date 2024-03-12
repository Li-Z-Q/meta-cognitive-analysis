import json
import tqdm
import os
import random
import openai
from datetime import datetime
import argparse
import time

# print(openai.Model.list())

def make_api_request(
    model,
    prompt, 
    temperature, 
    max_tokens,
    retries=3, 
):
    if model == "gpt-4":
        # print("Using gpt-4")
        # openai.api_base = "https://api.closeai-proxy.xyz/v1"
        # openai.api_key = "sk-nHmWcl3L1dsU7TGpf0LzdgOy1XWqswTZ4nB1CmastKr0B35e"
        openai.api_base = "http://8.219.106.213:5555/v1"
        openai.api_key = "sk-PCikBI1ZNOiaNH66C869CeE79cDe4fEeAe60F5597dE2Ac47"

    else:
        openai.api_base = "http://8.219.106.213:5555/v1"
        openai.api_key = "sk-l5f7ZkwzOKQtXPmvFfAf61Da27844fB6923dCcAeD8279183"
    
    retry_cnt = 0
    backoff_time = 30
    
    while retry_cnt <= retries:
        try:
            if '3.5' in model or model == 'gpt-4':
                completion = openai.ChatCompletion.create(
                    model=model,
                    messages=[
                        {"role": "user", "content": prompt}
                    ], 
                    temperature=temperature,
                    max_tokens=max_tokens,
                )
                
                if 1 == 1:
                    return completion.choices[0].message['content'].strip()
                else:
                    return [c.message['content'].strip() for c in completion.choices]
            elif '003' in model:
                completion = openai.Completion.create(
                    model=model,
                    prompt=prompt,
                    temperature=temperature,
                    max_tokens=max_tokens,
                )
                return completion.choices[0].text.strip()
        except Exception as e:
            print(f"OpenAIError: {e}.")
            if "Please reduce your prompt" in str(e):
                target_length = int(target_length * 0.8)
                print(f"Reducing target length to {target_length}, retrying...")
            else:
                print(f"Retrying in {backoff_time} seconds...")
                time.sleep(backoff_time)
                backoff_time *= 1.5
            retry_cnt += 1
            print("retry_cnt:", retry_cnt)
    

if __name__ == "__main__":
    model="gpt-3.5-turbo"
    # model="gpt-4"
    # model="text-davinci-003"
    
    temperature=1
    max_tokens=1024
    retries=3

    # question = "Would a Monoamine Oxidase candy bar cheer up a depressed friend?"
    
    # model_input = f"Keep necessary information and simplify the question below to reduce understanding difficulty. And explain why the new sentence is easier to understand.\n\nQuestion:\n{question}\n\nSimplified question:"
    
    model_input = \
r"""Generate a step-by-step reasoning process for each question and answer. Each step should include procedural information, which outlines the plan or method for that step, and factual information, which provides the necessary data or facts to execute the plan. Avoid repeating information from the question. The reasoning should be clear, logical, and based on the information provided in the question and answer.

Question: Where would you keep a rug near your front door? Choose from: A. persia, B. desk, C. table, D. living room, E. hall
Answer: D. living room
Reasoning: [["Consider where a rug might be kept near a front door in a house.", "A rug is a piece of cloth used to cover the floor."], ["Consider the nature of Persia.", "Persia is a historical and geographical place."], ["Consider the purpose of a desk.", "A desk is used as a workplace."], ["Consider the use of a table.", "A table is a piece of furniture used to hold items."], ["Consider what a living room is.", "The living room is a room in a house often located near the front door."], ["Consider the meaning of hall.", "A hall typically refers to a narrow passage or a larger public space in buildings."], ["Consider which of the above is the most likely place to keep a rug near the front door.", ""]]

Question: Danny found an old film in a sealed what? Choose from: A. clingfilm, B. disneyland, C. cave, D. cabinet, E. movie
Answer: D. cabinet
Reasoning: [["Consider where an old film might be found.", "An old film is always be found in a container"], ["Consider the meaning and using of clingfilm.", "Clingfilm is always used to wrap food."], ["Consider what Disneyland is.", "Disneyland is a theme park."], ["Consider the nature of a cave.", "Caves are natural formations in the earth."], ["Consider what a cabinet is.", "A cabinet is a storage place for various items."], ["Consider what a movie is.", "A movie is a form of entertainment to be watched."], ["Consider which of the above is the most likely place to find an old film.", ""]]

Question: The earth is one planet in what? Choose from: A. tree, B. orbit, C. solar system, D. fotograph, E. dreams
Answer: C. solar system
Reasoning: [["Consider the nature of the earth.", "The earth is a planet."], ["Consider what a tree is.", "A tree is a type of plant."], ["Consider the meaning of an orbit.", "An orbit is a path around a celestial body."], ["Consider what a solar system is.", "A solar system is a system of celestial bodies revolving around a star."], ["Consider the meaning of photograph.", "A photograph is a picture created using a camera."], ["Consider the nature of dreams.", "Dreams are images, ideas, emotions and sensations experienced during sleep."], ["Consider where the earth, as a planet, is located.", ""]]

Question: Who was the first woman ever to live? Choose from:\nA. God created Eve first.\nB. There was no first woman because humans evolved gradually.\nC. The first woman ever was Eve.\nD. The first people were Adam and Eve.
Reasoning:  
"""

    model_output = make_api_request(
        model=model,
        prompt=model_input,
        temperature=temperature,
        max_tokens=max_tokens,
        retries=retries
    )

    print(model_input)
    print("\nmodel_output:")
    print(model_output)