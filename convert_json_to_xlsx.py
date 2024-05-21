import json
import pandas as pd

with open('data.json', 'r') as file:
    data = json.load(file)

records = []

for line in data['lines']:
    combined_data = {**data, **line}
    combined_data.pop('lines', None)
    records.append(combined_data)

df = pd.DataFrame(records)

df.to_excel('output.xlsx', index=False)
