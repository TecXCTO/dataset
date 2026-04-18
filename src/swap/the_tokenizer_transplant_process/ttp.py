from transformers import AutoTokenizer, AutoModelForCausalLM

# 1. Define your source (high-capacity) and target (model to upgrade)
high_vocab_id = "google/gemma-4-31b" # The 256k+ vocab source
target_model_id = "meta-llama/Llama-3-8b" # The model you are upgrading

# 2. Load the high-capacity tokenizer
new_tokenizer = AutoTokenizer.from_pretrained(high_vocab_id)

# 3. Load the target model
model = AutoModelForCausalLM.from_pretrained(target_model_id)

# 4. Swap the tokenizer and resize embeddings
# This creates new memory 'slots' for the 256k tokens
model.resize_token_embeddings(len(new_tokenizer))

# 5. Save the 'transplanted' model
model.save_pretrained("./scientific-hybrid-model")
new_tokenizer.save_pretrained("./scientific-hybrid-model")

print(f"Swap complete. New vocab size: {len(new_tokenizer)}")
