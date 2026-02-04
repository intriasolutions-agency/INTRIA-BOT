
import csv
import requests
import io

url = "https://docs.google.com/spreadsheets/d/1VQHlNkH-GopAPP6VP-WvLc-Bl-Lkc8jrNAuNxTgLNZg/gviz/tq?tqx=out:csv&gid=91994935"
response = requests.get(url)
content = response.text

f = io.StringIO(content)
reader = csv.reader(f)
header = next(reader)

# The header has the values mixed in. Let's look for the row that actually contains headers properly or parse the first row.
# It seems the first row is: ['Identificador de URL 165-65r14-1hnsp ...', 'Nombre ...', ...]
# This means the values are separated by spaces within the cell.

identifiers = []
for col in header:
    if col.startswith('Identificador de URL'):
        # Split by space and remove the header part
        parts = col.split(' ')
        identifiers.extend(parts[3:]) # 'Identificador', 'de', 'URL' are the first 3

# Also read subsequent rows if they exist normally
for row in reader:
    if row and row[0]:
        identifiers.append(row[0])

with open('identifiers.txt', 'w') as f:
    for item in identifiers:
        if item.strip():
            f.write("%s\n" % item.strip())

print(f"Found {len(identifiers)} identifiers.")
