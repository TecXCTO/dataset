import json

# 1. Define your custom scientific symbols
scientific_symbols = ["Ω", "∫", "ħ", "∑", "Δ", "π", "∞", "√"]

# 2. Define standard special tokens
vocab = {
    "[PAD]": 0,
    "[UNK]": 1,
    "[CLS]": 2,
    "[SEP]": 3,
    "[MASK]": 4
}

# 3. Add your symbols to the vocabulary starting from index 5
for i, symbol in enumerate(scientific_symbols):
    vocab[symbol] = i + 5

# 4. Create the tokenizer.json structure
tokenizer_config = {
    "version": "1.0",
    "model": {
        "type": "WordLevel", # Ensures symbols are treated as whole tokens
        "vocab": vocab
    },
    "added_tokens": [
        {"id": v, "content": k, "single_word": True, "special": False}
        for k, v in vocab.items() if v >= 5
    ]
}

# 5. Save the files
with open("tokenizer.json", "w", encoding="utf-8") as f:
    json.dump(tokenizer_config, f, indent=2, ensure_ascii=False)

special_map = {
    "pad_token": "[PAD]",
    "unk_token": "[UNK]",
    "cls_token": "[CLS]",
    "sep_token": "[SEP]",
    "mask_token": "[MASK]"
}

with open("special_tokens_map.json", "w", encoding="utf-8") as f:
    json.dump(special_map, f, indent=2)

print("Files 'tokenizer.json' and 'special_tokens_map.json' have been created!")

