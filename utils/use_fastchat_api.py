"""Send a test message."""
import argparse
import json

import requests

from fastchat.model.model_adapter import get_conversation_template


def get_messages(model_name, worker_addr, message):

    conv = get_conversation_template(model_name)   
    conv.append_message(conv.roles[0], message)
    conv.append_message(conv.roles[1], None)
    prompt = conv.get_prompt()

    headers = {"User-Agent": "FastChat Client"}
    gen_params = {
        "model": model_name,
        "prompt": prompt,
        "temperature": 0,
        "max_new_tokens": 128,
        "stop": conv.stop_str,
        "stop_token_ids": conv.stop_token_ids,
        "echo": False,
    }
    response = requests.post(
        worker_addr + "/worker_generate",
        headers=headers,
        json=gen_params,
        stream=True,
    )
    print("response.text:")
    print(json.loads(response.text)['text'])

    response = requests.post(
        worker_addr + "/worker_get_conv_template",
        headers=headers,
        json=gen_params,
        stream=True,
    )
    print("response.text:")
    print(json.loads(response.text))


if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument(
    #     "--controller-address", type=str, default="http://124.16.138.150:1225"
    # )
    # parser.add_argument("--worker-address", type=str, default="http://124.16.138.150:1685")
    # parser.add_argument("--model-name", type=str, default="")
    # parser.add_argument("--temperature", type=float, default=0.0)
    # parser.add_argument("--max-new-tokens", type=int, default=128)
    # parser.add_argument(
    #     "--message", type=str, default="Tell me a story with more than 1000 words."
    # )
    # args = parser.parse_args()

    # main()

    # model_name = "vicuna-7b-v1.3"
    # model_name = "llama-7b"
    model_name = "one-shot"
    worker_addr = "http://124.16.138.142:1685"
    message = "Tell me a story with more than 1000 words."
    
    get_messages(model_name=model_name, worker_addr=worker_addr, message=message)