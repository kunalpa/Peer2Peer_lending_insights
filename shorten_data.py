"""
The large dataset will not fit into a single GitHub repo since it is ~1.6 GB
This python file takes a snapshot of the large file which is ~5% of the dataset.
The outputs are already in the notebook, so you don't really need to run it.
You can, but you will get worse results due to a smaller training set.
"""

import pandas as pd
from pathlib import Path

FULL_CSV_NAME = 'accepted_2007_to_2018Q4_full.csv'
CSV_NAME = 'accepted_2007_to_2018Q4.csv'

n = 20
print('reading csv')
df = pd.read_csv(FULL_CSV_NAME, skiprows=lambda i: i%n, low_memory=True)

print('writing to csv file')
filepath = Path(CSV_NAME)  
filepath.parent.mkdir(parents=True, exist_ok=True)  
df.to_csv(filepath)