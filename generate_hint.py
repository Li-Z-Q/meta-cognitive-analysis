import json
import random
from utils.use_gpt_api import make_api_request
random.seed(42)

def generate_hint_for_gsm8k(examples, data): # generate hint based on reference
    hint0p = '\n'.join(examples[0]['procedural-hint'])
    hint0f = '\n'.join(examples[0]['factual-hint'])
    in_context = \
f"""Generate procedural hint and factual hint for question based on reference. Each procedural hint outlines the plan or method for one step, and factual hint is a formula to execute the plan without any text or units. Each factual hint should be independent from each other. Avoid repeating information from the question.

Question: 
{examples[0]['question']}
Reference: 
{examples[0]['reference']}
Procedural hint: 
{hint0p}
Factual hint: 
{hint0f}"""

    model_input = in_context + f"\n\nQuestion:\n{data['question']}\nReference:\n{data['reference']}\nProcedural hint:"
    return model_input
    
def generate_hint_for_math1(examples, data): # generate hint based on reference
    hint0p = '\n'.join(examples[0]['procedural-hint'])
    hint0f = '\n'.join(examples[0]['factual-hint'])
    hint1p = '\n'.join(examples[1]['procedural-hint'])
    hint1f = '\n'.join(examples[1]['factual-hint'])
    hint2p = '\n'.join(examples[2]['procedural-hint'])
    hint2f = '\n'.join(examples[2]['factual-hint'])
    hint3p = '\n'.join(examples[3]['procedural-hint'])
    hint3f = '\n'.join(examples[3]['factual-hint'])
    in_context = \
f"""Create two types of hints for a question using a given reference as in the examples: 
1. Procedural Hint: Describe steps of how to solve the question. 
2. Factual Hint: Show necessary factual knowledge needed for solving each step. Do not include any procedural knowledge or question details in this hint. Each factual hint should not depend on any other hint. 
Use LaTeX for any formulas or symbols. 

Question: 
{examples[0]['question']}
Reference: 
{examples[0]['reference']}
Procedural hint: 
{hint0p}
Factual hint: 
{hint0f}

Question: 
{examples[1]['question']}
Reference: 
{examples[1]['reference']}
Procedural hint: 
{hint1p}
Factual hint: 
{hint1f}

Question: 
{examples[2]['question']}
Reference: 
{examples[2]['reference']}
Procedural hint: 
{hint2p}
Factual hint: 
{hint2f}

Question: 
{examples[3]['question']}
Reference: 
{examples[3]['reference']}
Procedural hint: 
{hint3p}
Factual hint: 
{hint3f}"""

    model_input = in_context + f"\n\nQuestion:\n{data['question']}\nReference:\n{data['reference']}\nProcedural hint:"
    return model_input

def generate_hint_for_math2(examples, data): # generate hint based on reference
    hint0p = '\n'.join(examples[0]['procedural-hint'])
    hint0f = '\n'.join(examples[0]['factual-hint'])
    hint1p = '\n'.join(examples[1]['procedural-hint'])
    hint1f = '\n'.join(examples[1]['factual-hint'])
    hint2p = '\n'.join(examples[2]['procedural-hint'])
    hint2f = '\n'.join(examples[2]['factual-hint'])
    hint3p = '\n'.join(examples[3]['procedural-hint'])
    hint3f = '\n'.join(examples[3]['factual-hint'])
    in_context = \
f"""Create two types of hints for a question using a given reference as in the examples: 
1. Procedural Hint: Describe steps of how to solve the question. 
2. Factual Hint: Show necessary factual knowledge needed for solving each step. Do not include any procedural knowledge or question details in this hint. Each factual hint should not depend on any other hint. 
Use LaTeX for any formulas or symbols. 

Question: 
{examples[0]['question']}
Reference: 
{examples[0]['reference']}
Procedural hint: 
{hint0p}
Factual hint: 
{hint0f}

Question: 
{examples[1]['question']}
Reference: 
{examples[1]['reference']}
Procedural hint: 
{hint1p}
Factual hint: 
{hint1f}

Question: 
{examples[2]['question']}
Reference: 
{examples[2]['reference']}
Procedural hint: 
{hint2p}
Factual hint: 
{hint2f}

Question: 
{examples[3]['question']}
Reference: 
{examples[3]['reference']}
Procedural hint: 
{hint3p}
Factual hint: 
{hint3f}"""

    model_input = in_context + f"\n\nQuestion:\n{data['question']}\nReference:\n{data['reference']}\nProcedural hint:"
    return model_input
  
def generate_hint_for_math3(examples, data): # generate hint based on reference
    hint0p = '\n'.join(examples[0]['procedural-hint'])
    hint0f = '\n'.join(examples[0]['factual-hint'])
    hint1p = '\n'.join(examples[1]['procedural-hint'])
    hint1f = '\n'.join(examples[1]['factual-hint'])
    hint2p = '\n'.join(examples[2]['procedural-hint'])
    hint2f = '\n'.join(examples[2]['factual-hint'])
    hint3p = '\n'.join(examples[3]['procedural-hint'])
    hint3f = '\n'.join(examples[3]['factual-hint'])
    in_context = \
f"""Create two types of hints for a question using a given reference as in the examples: 
1. Procedural Hint: Describe steps of how to solve the question. 
2. Factual Hint: Show necessary factual knowledge needed for solving each step. Do not include any procedural knowledge or question details in this hint. Each factual hint should not depend on any other hint. 
Use LaTeX for any formulas or symbols. 

Question: 
{examples[0]['question']}
Reference: 
{examples[0]['reference']}
Procedural hint: 
{hint0p}
Factual hint: 
{hint0f}

Question: 
{examples[1]['question']}
Reference: 
{examples[1]['reference']}
Procedural hint: 
{hint1p}
Factual hint: 
{hint1f}

Question: 
{examples[2]['question']}
Reference: 
{examples[2]['reference']}
Procedural hint: 
{hint2p}
Factual hint: 
{hint2f}

Question: 
{examples[3]['question']}
Reference: 
{examples[3]['reference']}
Procedural hint: 
{hint3p}
Factual hint: 
{hint3f}"""

    model_input = in_context + f"\n\nQuestion:\n{data['question']}\nReference:\n{data['reference']}\nProcedural hint:"
    return model_input

def generate_hint_for_truthfulqa(examples, data): # p_hint is think about each option, f_hint is the fact to surport ot not the option
    hint0p = '\n'.join(examples[0]['procedural-hint'])
    hint0f = '\n'.join(examples[0]['factual-hint'])
    hint1p = '\n'.join(examples[1]['procedural-hint'])
    hint1f = '\n'.join(examples[1]['factual-hint'])
    in_context = \
f"""Generate procedural hint and factual hint for question based on the answer. procedural hint is "Use known knowledge to determine which option is correct.", and factual hint provides facts about each option. The factual hint should not include any reasoning or conclusion about this question. Each factual hint should be independent from each other.

Question: 
{examples[0]['question']}
Answer: 
{examples[0]['answer']}
Procedural hint: 
{hint0p}
Factual hint: 
{hint0f}

Question: 
{examples[1]['question']}
Answer: 
{examples[1]['answer']}
Procedural hint: 
{hint1p}
Factual hint: 
{hint1f}"""

    model_input = in_context + f"\n\nQuestion:\n{data['question']}\nAnswer:\n{data['answer']}\nProcedural hint:"
    return model_input

def generate_hint_for_arceasy(examples, data): # p_hint is think about question, f_hint is the answer
    hint0p = '\n'.join(examples[0]['procedural-hint'])
    hint0f = '\n'.join(examples[0]['factual-hint'])
    hint1p = '\n'.join(examples[1]['procedural-hint'])
    hint1f = '\n'.join(examples[1]['factual-hint'])
    in_context = \
f"""Generate procedural hint and factual hint for question based on the answer. procedural hint is a plan to think about the object thing in question, and factual hint provides facts for this plan. The factual hint should not include any reasoning or conclusion about this question. Each factual hint should be independent from each other.

Question: 
{examples[0]['question']}
Answer: 
{examples[0]['answer']}
Procedural hint: 
{hint0p}
Factual hint: 
{hint0f}

Question: 
{examples[1]['question']}
Answer: 
{examples[1]['answer']}
Procedural hint: 
{hint1p}
Factual hint: 
{hint1f}"""

    model_input = in_context + f"\n\nQuestion:\n{data['question']}\nAnswer:\n{data['answer']}\nProcedural hint:"
    return model_input

def generate_hint_for_arcchallenge(examples, data): # p_hint is 1. think about question, 2. think about each option, f_hint is the answer
    hint0p = '\n'.join(examples[0]['procedural-hint'])
    hint0f = '\n'.join(examples[0]['factual-hint'])
    hint1p = '\n'.join(examples[1]['procedural-hint'])
    hint1f = '\n'.join(examples[1]['factual-hint'])
    in_context = \
f"""Generate procedural hint and factual hint for question based on the answer. procedural hint includes two plans, the first plan is to think about the question, while the second plan is to think about each option, and factual hint provides the necessary data or facts to execute the plan. The factual hint should not include any reasoning or conclusion about this question. Each factual hint should be independent from each other.

Question: 
{examples[0]['question']}
Answer: 
{examples[0]['answer']}
Procedural hint: 
{hint0p}
Factual hint: 
{hint0f}

Question: 
{examples[1]['question']}
Answer: 
{examples[1]['answer']}
Procedural hint: 
{hint1p}
Factual hint: 
{hint1f}"""

    model_input = in_context + f"\n\nQuestion:\n{data['question']}\nAnswer:\n{data['answer']}\nProcedural hint:"
    return model_input
      
def generate_hint_for_csqa(examples, data): # p_hint is 1. think about question, 2. think about each option, f_hint is the answer
    hint0p = '\n'.join(examples[0]['procedural-hint'])
    hint0f = '\n'.join(examples[0]['factual-hint'])
    hint1p = '\n'.join(examples[1]['procedural-hint'])
    hint1f = '\n'.join(examples[1]['factual-hint'])
    in_context = \
f"""Generate procedural hint and factual hint for question based on the answer. procedural hint includes two plans, the first plan is to think about the question, while the second plan is to think about each option, and factual hint provides the necessary data or facts to execute the plan. The factual hint should not include any reasoning or conclusion about this question. Each factual hint should be independent from each other.

Question: 
{examples[0]['question']}
Answer: 
{examples[0]['answer']}
Procedural hint: 
{hint0p}
Factual hint: 
{hint0f}

Question: 
{examples[1]['question']}
Answer: 
{examples[1]['answer']}
Procedural hint: 
{hint1p}
Factual hint: 
{hint1f}"""

    model_input = in_context + f"\n\nQuestion:\n{data['question']}\nAnswer:\n{data['answer']}\nProcedural hint:"
    return model_input

def generate_hint_for_mmluhuman(examples, data): # p_hint is 1. think about question, 2. think about each option, f_hint is the answer
    hint0p = '\n'.join(examples[0]['procedural-hint'])
    hint0f = '\n'.join(examples[0]['factual-hint'])
    hint1p = '\n'.join(examples[1]['procedural-hint'])
    hint1f = '\n'.join(examples[1]['factual-hint'])
    in_context = \
f"""Generate procedural hint and factual hint for question based on the answer. procedural hint includes two plans, the first plan is to think about the question, while the second plan is to think about each option, and factual hint provides the necessary data or facts to execute the plan. The factual hint should not include any reasoning or conclusion about this question. Each factual hint should be independent from each other.

Question: 
{examples[0]['question']}
Answer: 
{examples[0]['answer']}
Procedural hint: 
{hint0p}
Factual hint: 
{hint0f}

Question: 
{examples[1]['question']}
Answer: 
{examples[1]['answer']}
Procedural hint: 
{hint1p}
Factual hint: 
{hint1f}"""

    model_input = in_context + f"\n\nQuestion:\n{data['question']}\nAnswer:\n{data['answer']}\nProcedural hint:"
    return model_input

def generate_hint_for_mmluother(examples, data): # p_hint is 1. think about question, 2. think about each option, f_hint is the answer
    hint0p = '\n'.join(examples[0]['procedural-hint'])
    hint0f = '\n'.join(examples[0]['factual-hint'])
    hint1p = '\n'.join(examples[1]['procedural-hint'])
    hint1f = '\n'.join(examples[1]['factual-hint'])
    in_context = \
f"""Generate procedural hint and factual hint for question based on the answer. procedural hint includes two plans, the first plan is to think about the question, while the second plan is to think about each option, and factual hint provides the necessary data or facts to execute the plan. The factual hint should not include any reasoning or conclusion about this question. Each factual hint should be independent from each other.

Question: 
{examples[0]['question']}
Answer: 
{examples[0]['answer']}
Procedural hint: 
{hint0p}
Factual hint: 
{hint0f}

Question: 
{examples[1]['question']}
Answer: 
{examples[1]['answer']}
Procedural hint: 
{hint1p}
Factual hint: 
{hint1f}"""

    model_input = in_context + f"\n\nQuestion:\n{data['question']}\nAnswer:\n{data['answer']}\nProcedural hint:"
    return model_input

def generate_hint_for_mmlusocial(examples, data): # p_hint is 1. think about question, 2. think about each option, f_hint is the answer
    hint0p = '\n'.join(examples[0]['procedural-hint'])
    hint0f = '\n'.join(examples[0]['factual-hint'])
    hint1p = '\n'.join(examples[1]['procedural-hint'])
    hint1f = '\n'.join(examples[1]['factual-hint'])
    in_context = \
f"""Generate procedural hint and factual hint for question based on the answer. procedural hint includes two plans, the first plan is to think about the question, while the second plan is to think about each option, and factual hint provides the necessary data or facts to execute the plan. The factual hint should not include any reasoning or conclusion about this question. Each factual hint should be independent from each other.

Question: 
{examples[0]['question']}
Answer: 
{examples[0]['answer']}
Procedural hint: 
{hint0p}
Factual hint: 
{hint0f}

Question: 
{examples[1]['question']}
Answer: 
{examples[1]['answer']}
Procedural hint: 
{hint1p}
Factual hint: 
{hint1f}"""

    model_input = in_context + f"\n\nQuestion:\n{data['question']}\nAnswer:\n{data['answer']}\nProcedural hint:"
    return model_input

def generate_hint_for_mmlustem(examples, data): # p_hint is 1. think about question, 2. think about each option, f_hint is the answer
    hint0p = '\n'.join(examples[0]['procedural-hint'])
    hint0f = '\n'.join(examples[0]['factual-hint'])
    hint1p = '\n'.join(examples[1]['procedural-hint'])
    hint1f = '\n'.join(examples[1]['factual-hint'])
    
    in_context = \
f"""Generate procedural hint and factual hint for question based on the answer. procedural hint includes two plans, the first plan is to think about the question, while the second plan is to think about each option, and factual hint provides the necessary data or facts to execute the plan. The factual hint should not include any reasoning or conclusion about this question. Each factual hint should be independent from each other.

Question: 
{examples[0]['question']}
Answer: 
{examples[0]['answer']}
Procedural hint: 
{hint0p}
Factual hint: 
{hint0f}

Question: 
{examples[1]['question']}
Answer: 
{examples[1]['answer']}
Procedural hint: 
{hint1p}
Factual hint: 
{hint1f}"""

    model_input = in_context + f"\n\nQuestion:\n{data['question']}\nAnswer:\n{data['answer']}\nProcedural hint:"
    return model_input

if __name__ == "__main__":

    for dataset_name in ["math3"]: # 
        print(dataset_name)
        
        examples = json.load(open('datas/examples/{0}_examples.json'.format(dataset_name)))
        raw_datas = json.load(open('datas/raw_datas/{0}_raw.json'.format(dataset_name)))
        save_file = open('datas/datas_with_hint/{0}_with_hint_no_filter.jsonl'.format(dataset_name), 'a')
        save_file_complete = open('datas/datas_with_hint/{0}_with_hint_no_filter_complete.jsonl'.format(dataset_name), 'a')
        already_datas_questions = [json.loads(l)['question'] for l in open('datas/datas_with_hint/{0}_with_hint_no_filter.jsonl'.format(dataset_name)).readlines()]
        print("len(already_datas_questions):", len(already_datas_questions))
        
        i = 0
        for data in raw_datas:    
            
            examples = random.sample(examples, 4)

            if data['question'] in already_datas_questions:
                continue
                    
            if dataset_name == 'gsm8k':
                model_input = generate_hint_for_gsm8k(examples, data)
            elif dataset_name == 'csqa':
                model_input = generate_hint_for_csqa(examples, data)
            elif dataset_name == 'truthfulqa':
                model_input = generate_hint_for_truthfulqa(examples, data)
            elif dataset_name == 'arceasy':
                model_input = generate_hint_for_arceasy(examples, data)
            elif dataset_name == 'arcchallenge':
                model_input = generate_hint_for_arcchallenge(examples, data)
            elif dataset_name == 'math1':
                model_input = generate_hint_for_math1(examples, data)
            elif dataset_name == 'math2':
                model_input = generate_hint_for_math2(examples, data)
            elif dataset_name == 'math3':
                model_input = generate_hint_for_math3(examples, data)
            elif dataset_name == 'mmluhuman':
                model_input = generate_hint_for_mmluhuman(examples, data)
            elif dataset_name == 'mmluother':
                model_input = generate_hint_for_mmluother(examples, data)
            elif dataset_name == 'mmlusocial':
                model_input = generate_hint_for_mmlusocial(examples, data)
            elif dataset_name == 'mmlustem':
                model_input = generate_hint_for_mmlustem(examples, data)
            else:
                raise NotImplementedError
            
            model_output = make_api_request(
                model='gpt-4',
                prompt=model_input,
                temperature=1,
                max_tokens=512,
                retries=3
            )
            
            # print(model_input)
            # print(model_output)
            save_file_complete.write(json.dumps({"model_input": model_input, "model_output": model_output}, ensure_ascii=False) + '\n')
            
            model_output = model_output.strip()
            try:
                model_output = model_output.split('Factual hint:')
                data['procedural-hint'] = model_output[0].strip().split('\n')
                data['factual-hint'] = model_output[1].strip().split('\n')
            except Exception as e:
                print(e)
                print(model_output)
                continue
            
            save_file.write(json.dumps(data, ensure_ascii=False) + '\n')
            save_file.flush()
            i += 1
            if i == 120:
                break
            
            # break

        save_file.close()
        
print("Done!")
