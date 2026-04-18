import json
import random

def generate_scientific_dataset(output_file, num_samples=1000):
    # Mapping concepts to symbols for the model to learn relationships
    templates = [
        {"prompt": "Calculate the integral of {var} with respect to x.", "completion": "The expression is written as: ∫ {var} dx."},
        {"prompt": "Find the gradient of the field {var}.", "completion": "The gradient vector is ∇{var}."},
        {"prompt": "What is the summation of the series up to {n}?", "completion": "This is denoted as ∑_{{i=1}}^{{{n}}} a_i."},
        {"prompt": "How do we represent the reduced Planck constant?", "completion": "In quantum mechanics, it is represented as ħ."},
        {"prompt": "Show the change in variable {var}.", "completion": "The change is denoted by the symbol Δ{var}."},
        {"prompt": "What is the partial derivative of f with respect to {var}?", "completion": "It is written as ∂f/∂{var}."}
    ]

    vars_list = ["x", "y", "t", "Ψ", "Φ", "θ", "ρ"]
    
    with open(output_file, "w", encoding="utf-8") as f:
        for _ in range(num_samples):
            tpl = random.choice(templates)
            var = random.choice(vars_list)
            n_val = random.randint(10, 100)
            
            # Fill the template
            p = tpl["prompt"].format(var=var, n=n_val)
            c = tpl["completion"].format(var=var, n=n_val)
            
            # Write as a single JSON line (JSONL format)
            json_line = json.dumps({"prompt": p, "completion": c}, ensure_ascii=False)
            f.write(json_line + "\n")

# Generate 5,000 examples for your training run
generate_scientific_dataset("scientific_train_data.jsonl", num_samples=5000)
print("Training file 'scientific_train_data.jsonl' created successfully.")

