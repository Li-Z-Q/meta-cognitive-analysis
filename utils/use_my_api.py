import time
import requests
import json
from deploy.deploy_model import model_port

# requests = requests.Session()
# requests.trust_env = False


def get_loss(text, instruction, url, model_name):
    
    print('\n')
    print("------------------------------------input-------------------------------------------")
    print("------------------------------------------------------------------------------------")
    print(instruction)
    print(text)
    
    start_time = time.time()
    model_input = {
        "text": text, 
        "instruction": instruction,
        "system_prompt": "",
    }
    
    port = model_port[model_name]
    response = requests.post("{0}:{1}/complete".format(url, port), json=model_input)
    
    print(response)
    
    model_output = response.text
    model_output = json.loads(model_output)
    model_output = float(model_output)
    
    print("---------------------")
    print(model_output)
    used_time = time.time() - start_time
    print(f"used time: {used_time}")
    # input("Press Enter to continue...")
    
    return model_output




def get_messages(text, url, model_name, do_sample=False, max_new_tokens=512):
    
    print('\n')
    print("------------------------------------input-------------------------------------------")
    print("------------------------------------------------------------------------------------")
    print(text)
    
    start_time = time.time()
    model_input = {
        "text": text, 
        "system_prompt": "",
        "do_sample": do_sample,
        "temperature": 1,
        "max_new_tokens": max_new_tokens,
    }
    
    port = model_port[model_name]
    response = requests.post("{0}:{1}/complete".format(url, port), json=model_input)
    
    print(response)
    
    model_output = response.text
    
    model_output = json.loads(model_output)
    
    print("---------------------")
    print(model_output)
    used_time = time.time() - start_time
    print(f"used time: {used_time}")
    # input("Press Enter to continue...")
    
    return model_output[len(text):].strip()


if __name__ == "__main__":
    model_name = "vicuna-7b-v1.3"
    url = "http://124.16.138.150"
    message = "Tell me a story with more than 1000 words."
    # message = "A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions.\n" + message
    
    r = get_messages(message, url, model_name)