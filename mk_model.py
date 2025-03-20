import pandas as pd
import torch
from transformers import BertForSequenceClassification, AutoTokenizer, TrainingArguments, Trainer
from datasets import Dataset

from transformers import AutoModelForCausalLM, AutoTokenizer

# ✅ LLaMA 계열 모델 사용 (Hugging Face 모델 경로 확인 후 수정 가능)
model_name = "yanolja/EEVE-Korean-10.8B-v1.0"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# ✅ CSV 데이터를 불러와서 학습
df = pd.read_csv("/mnt/hdd1/moon/ev_data/dataset/merged_dataset.csv")
dataset = Dataset.from_pandas(df)

def tokenize_function(example):
    return tokenizer(example["text"], padding="max_length", truncation=True)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

training_args = TrainingArguments(
    output_dir="./finetuned_model",
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    num_train_epochs=3,
    save_strategy="epoch"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets,
    eval_dataset=tokenized_datasets
)

trainer.train()

# ✅ 학습된 모델 저장
model.save_pretrained("/mnt/hdd1/moon/llm/korModel/csv-finetuned")
tokenizer.save_pretrained("/mnt/hdd1/moon/llm/korModel/csv-finetuned")
