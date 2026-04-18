"""
Merging Scientific Tokens
This script loads an existing tokenizer and adds your symbols. Crucially, it also resizes the model's embedding layer—without this step, the model will crash because it won't have "space" in its brain for the new symbols. 
"""
from transformers import AutoTokenizer, AutoModelForCausalLM
import json

# 1. Load your existing model and tokenizer
model_id = "meta-llama/Llama-2-7b-hf" # Replace with your model
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

# 2. Load symbols from your text file
with open("symbols.txt", "r", encoding="utf-8") as f:
    custom_symbols = [line.strip() for line in f if line.strip()]

# 3. Add symbols as 'Special Tokens'
# This prevents subword tokenization from splitting them
num_added_toks = tokenizer.add_tokens(custom_symbols, special_tokens=True)
print(f"Added {num_added_toks} scientific tokens.")

# 4. CRITICAL: Resize model embeddings to match the new tokenizer size
model.resize_token_embeddings(len(tokenizer))

# 5. Save the updated tokenizer and model
tokenizer.save_pretrained("./scientific-model-tokenizer")
model.save_pretrained("./scientific-model-base")

print("Updated tokenizer.json and model weights saved successfully!")

