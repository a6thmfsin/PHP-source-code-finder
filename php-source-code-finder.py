import re
import requests
from tqdm import tqdm

inputfile = "input.txt"
outputfile = "output.txt"

def check_php_source_code(url):
    try:
        response = requests.get(url)
        if "<?php" in response.text:
            print(f"Found backend source code: {url}")
    except requests.RequestException as e:
        print(f"Request error: {url}: {e}")

with open(inputfile, 'r') as infile, open(outputfile, 'w') as outfile:
    for line in tqdm(infile, desc="Changed & tested urls ", unit=" lines"):
        modified_line = re.sub(r'(\.php).*', r'\1~', line)
        outfile.write(modified_line.strip() + '\n')
        url = modified_line.strip()
        check_php_source_code(url)

print(f"{outputfile}")
