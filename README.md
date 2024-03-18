# meta-cognitive-analysis

Meta-Cognitive Analysis: Evaluating Declarative and Procedural Knowledge in Datasets and Large Language Models

#### Prepare Experimental Datasets
```bash
python generate_raw_datas.py
```

#### Generate Hint via GPT4 and GPT3.5
```bash
# Generate Hint by In-Context Learning
python generate_hint.py
# Generate Some Noisy Factual Hint for MATH and GSM8k
python generate_noise.py
```

#### Evaluate by Hint Injection
```bash
# Include No Hint, Factual Hint, Procedural Hint, Both Factual and Procedural Hint
bash run.sh
```

#### Analyze Results
```bash
# Annotate via Some Rules
python annotate.py
# Show Improvement Scores from Hint Injection
python analysis.py
```