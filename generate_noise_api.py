import random
random.seed(42)
import json
from utils.use_gpt_api import make_api_request

def IsFloatNum(str):
    s=str.split('.')
    if len(s)>2:
        return False
    else:
        for si in s:
            if not si.isdigit():
                return False
        return True

            
def generate_noise_gsm8k(facts):
# facts:
# "12 - 8 = 4",
# "30 + 20 = 50",
# "8 / 3 = 2.66",
# "30 + 24 = 54",
# "12 + 8 = 20",
# "4 + 2 = 6"
    noices = []
    num_list = []
    for fact in facts:
        nums = fact.split(' ')
        for num in nums:
            if IsFloatNum(num) and num not in num_list:
                num_list.append(num)    
    
    


if __name__ == "__main__":
# Generate two relevant facts based on give fact as in the examples. Do not generate facts that have the same meaning as the given fact.

    for dataset_name in ["math1", "math2", "math3"]:
        
        examples = json.load(open('datas/examples/{0}_examples.json'.format(dataset_name)))
        examples = random.sample(examples, 3)
        raw_datas = json.load(open('datas/datas_with_hint/{0}_final.json'.format(dataset_name)))
        save_file = open('datas/datas_with_hint/{0}_final_with_noise.jsonl'.format(dataset_name), 'w')

        # for data in raw_datas:
        #     data['noisy-factual-hint'] = examples[0]['noisy-factual-hint']
        #     save_file.write(json.dumps(data, ensure_ascii=False) + '\n')
        #     save_file.flush()
        # save_file.close()

        fact0 = '\n'.join(examples[0]['factual-hint'])
        noisy_fact0 = '\n'.join(examples[0]['noisy-factual-hint'])
        fact1 = '\n'.join(examples[1]['factual-hint'])
        noisy_fact1 = '\n'.join(examples[1]['noisy-factual-hint'])
        
        in_context = \
f"""Generate some correct facts as noise that are similar to the given facts.

Facts:
{fact0}
Noisy facts:
{noisy_fact0}

Facts:
{fact1}
Noisy facts:
{noisy_fact1}

"""
# TODO
        for data in raw_datas:
            if data['factual-hint'] == []:
                continue
            
            fact = '\n'.join(data['factual-hint'])
            
            model_input = in_context + "Facts:\n{0}\nNoisy facts:".format(fact)
            model_output = make_api_request(
                model='gpt-4',
                prompt=model_input,
                temperature=1,
                max_tokens=512,
                retries=3
            )

            noisy_factual_hint = model_output.split('\n')

            data['noisy-factual-hint'] = noisy_factual_hint
            
            save_file.write(json.dumps(data, ensure_ascii=False) + '\n')
            save_file.flush()

        save_file.close()