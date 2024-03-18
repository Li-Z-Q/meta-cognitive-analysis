time1=$(date "+%Y-%m-%d %H:%M:%S")
echo "time1: ${time1}"
# source activate
# conda activate py310
url_id=144
model_name=baichuan-7b-02420 # gpt3.5 # codellama-13b-instruct # vicuna-33b-v1.3 # llama-65b # llama-2-7b # llama-13b # llama-7b # vicuna-13b-v1.3 # llama-30b  # llama-2-13b # llama-2-7b-chat # llama-2-13b-chat # falcon-7b # falcon-7b-instruct # baichuan-7b-00880
echo "${model_name} start, url: ${url_id}"
for hint_type in no_hint procedural_hint   factual_hint procedural_factual_hint     #   
do
for dataset_name in "multiarith" "gsm8k" "csqa" "truthfulqa" "arceasy" "arcchallenge" "math1" "math2" "math3" "mmluhuman" "mmluother" "mmlusocial" "mmlustem" 
do
python -u test_${hint_type}.py \
    --url_id ${url_id} \
    --model_name ${model_name} \
    --dataset_name ${dataset_name} \
> logs/${model_name}_${dataset_name}_${hint_type}.log              
echo "${model_name}_${dataset_name}_${hint_type} done"
done
done    
echo "all Done!"   

time2=$(date "+%Y-%m-%d %H:%M:%S")
echo "time2: ${time2}"