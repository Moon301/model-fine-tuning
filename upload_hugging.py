from ctransformers.convert import convert_hf_model

convert_hf_model(
    model_name="/mnt/hdd1/moon/llm/korModel/csv-finetuned",
    output_path="/mnt/hdd1/moon/llm/korModel/csv-gguf",
    model_type="llama"
)


