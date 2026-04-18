import requests
import xml.etree.ElementTree as ET
import json
import time

def scrape_arxiv_to_jsonl(category="physics.gen-ph", max_results=50, output_file="arxiv_scientific_data.jsonl"):
    # Base URL for ArXiv API
    base_url = f'http://arxiv.org:{category}&start=0&max_results={max_results}'
    
    response = requests.get(base_url)
    if response.status_code != 200:
        print("Failed to fetch data from ArXiv.")
        return

    # Parse XML response
    root = ET.fromstring(response.content)
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    entries = root.findall('atom:entry', ns)

    with open(output_file, "a", encoding="utf-8") as f:
        for entry in entries:
            title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
            summary = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')
            
            # Format as a training pair: Title -> Summary (Abstract)
            data_pair = {
                "instruction": f"Summarize the following scientific research titled: {title}",
                "context": "",
                "response": summary
            }
            
            f.write(json.dumps(data_pair, ensure_ascii=False) + "\n")
            
    print(f"Successfully scraped {len(entries)} abstracts into {output_file}.")

# Categories to try: 'math.MP' (Math Physics), 'physics.quant-ph' (Quantum), 'math.CA' (Calculus)
scrape_arxiv_to_jsonl(category="math.MP", max_results=100)

if __name__=="__main__":
    categories = ["math.MP", "quant-ph", "math.CA"]
    for cat in categories:
        print(f"Scraping {cat}...")
        scrape_arxiv_to_jsonl(category=cat, max_results=100, output_file="final_scientific_dataset.jsonl")
    
