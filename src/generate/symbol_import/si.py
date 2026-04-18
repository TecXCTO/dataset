import json

# Replace 'symbols.txt' with the actual path to your file
input_file = "symbols.txt" 

def build_scientific_tokenizer(file_path):
    # 1. Load symbols from your file
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            # Reads each line, strips whitespace, and removes empty lines/duplicates
            symbols = list(dict.fromkeys([line.strip() for line in f if line.strip()]))
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return

    # 2. Define standard special tokens (essential for model training)
    vocab = {
        "[PAD]": 0,
        "[UNK]": 1,
        "[CLS]": 2,
        "[SEP]": 3,
        "[MASK]": 4
    }

    # 3. Append your custom symbols to the vocabulary
    for i, symbol in enumerate(symbols):
        vocab[symbol] = i + 5

    # 4. Construct the main tokenizer.json structure
    tokenizer_config = {
        "version": "1.0",
        "model": {
            "type": "WordLevel", 
            "vocab": vocab
        },
        "added_tokens": [
            {"id": v, "content": k, "single_word": True, "special": False}
            for k, v in vocab.items() if v >= 5
        ]
    }

    # 5. Export files with UTF-8 encoding to protect Unicode symbols
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

    print(f"Success! {len(symbols)} symbols processed into tokenizer files.")

build_scientific_tokenizer(input_file)

