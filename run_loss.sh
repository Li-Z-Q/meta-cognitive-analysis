url_id=150
model_name=codellama-13b-instruct # codellama-13b-instruct # vicuna-33b-v1.3 # llama-65b # llama-2-7b # llama-13b_load_in_8bit # llama-7b # vicuna-13b-v1.3 # llama-30b  # llama-2-13b # llama-2-7b-chat # llama-2-13b-chat # falcon-7b # falcon-7b-instruct
echo "${model_name} start"
for hint_type in procedural factual understanding # factual_hint_noise procedural_factual_hint_noise no_hint_zero
do
for dataset_name in "gsm8k" "csqa" "truthfulqa" "arceasy" "arcchallenge" "math1" "math2" "math3" "mmluhuman" "mmluother" "mmlusocial" "mmlustem"
do
python -u test_loss_${hint_type}.py \
    --url_id ${url_id} \
    --model_name ${model_name} \
    --dataset_name ${dataset_name} \
> logs/loss_${model_name}_${dataset_name}_${hint_type}.log
echo "${model_name}_${dataset_name}_${hint_type} done"
done
done    
echo "all Done!"