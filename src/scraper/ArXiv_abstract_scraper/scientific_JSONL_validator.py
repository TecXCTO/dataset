import json

def validate_scientific_dataset(file_path):
    # Core symbols to track
    symbols_to_verify = ["∫", "∇", "Δ", "ħ", "∑", "π", "∂", "√"]
    stats = {s: 0 for s in symbols_to_verify}
    valid_count = 0
    error_lines = []

    print(f"--- Validating {file_path} ---")
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                try:
                    data = json.loads(line)
                    valid_count += 1
                    
                    # Search for symbol presence in the content
                    content_str = json.dumps(data, ensure_ascii=False)
                    for symbol in symbols_to_verify:
                        if symbol in content_str:
                            stats[symbol] += 1
                            
                except json.JSONDecodeError:
                    error_lines.append(i + 1)

        # Output Results
        print(f"Total Lines Processed: {valid_count + len(error_lines)}")
        print(f"Successfully Parsed JSON Lines: {valid_count}")
        
        if error_lines:
            print(f"❌ JSON Syntax Errors on lines: {error_lines}")
        else:
            print("✅ No JSON syntax errors found.")

        print("\n--- Symbol Presence Count ---")
        for symbol, count in stats.items():
            status = "✅" if count > 0 else "⚠️ (Not found)"
            print(f"{symbol} : {count} occurrences {status}")

    except Exception as e:
        print(f"Critical Error: {e}")

# Run validation on your generated file
validate_scientific_dataset("final_scientific_dataset.jsonl")

