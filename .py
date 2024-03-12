import pandas as pd
import numpy as np
import math


batch1 = pd.read_csv("/Users/cjz/Downloads/HC AI intern (Trevor)/ACTUAL/Task3/input_csv/Batch1_Extraction_IssueCategorization - Batch1_Ground_Truth.csv")
batch2 = pd.read_csv("/Users/cjz/Downloads/HC AI intern (Trevor)/ACTUAL/Task3/input_csv/Batch2_Extraction_IssueCategorization - Batch2_GT.csv")

batch1 = batch1.rename(columns={batch1.columns[i]: batch1.columns[i].lower() for i in range(len(batch1.columns))})
batch2 = batch2.rename(columns={batch2.columns[i]: batch2.columns[i].lower() for i in range(len(batch2.columns))})

batch1.head()



df1_cols = list(batch1.columns)
df2_cols = list(batch2.columns)

# df1 = columns from batch 1; df2 = columns from batch 2
verified_cols = []

if len(df1_cols) < len(df2_cols): # check if there are any columns already by the same name
    for col in df1_cols: 
        if col in df2_cols:
            verified_cols.append(col)
else:
    for col in df2_cols:
        if col in df1_cols:
            verified_cols.append(col)

for col in verified_cols: # remove these cols from each list
    df1_cols.remove(col)
    df2_cols.remove(col)

print(df1_cols)
print(df2_cols, "\n")

print(batch1.columns)
print(batch2.columns)



#matches = [[match] for match in df1_cols]

counter = -1
valid = []

# algorithm to find longest common substring
for col1 in df1_cols:
    counter += 1
    for col2 in df2_cols:
        matrix = [[0 for i in range(len(col1))] for j in range(len(col2))] # two dimensions to represent two words
        highest = 0 # var to store length of longest substring
        for loc1 in range(len(col1)):
            for loc2 in range(len(col2)):
                if col1[loc1] == col2[loc2]:
                    matrix[loc2][loc1] = matrix[loc2 - 1][loc1 - 1] + 1
                if matrix[loc2][loc1] > highest:
                    highest = matrix[loc2][loc1]
        if highest > 6:
            valid.append([col1, col2, highest])

print(valid)

unique = []


for group in valid:
    for loc in range(2):
        if group[loc] not in unique:
            unique.append(group[loc])
            
matches = []
for idx in range(len(unique)):
    matches.append([])
    for group in range(len(valid)):
        if unique[idx] in valid[group]:
            matches[idx] += [[group, valid[group][2]]]
    if len(matches) == 2:
        pass
    
print(matches)

print(len(max(matches, key=len)))
while len(max(matches, key=len)) > 1:
    for idx in range(len(matches)):
        if len(matches[idx]) == len(max(matches, key=len)):
            max_idx = 0
            for idx2 in range(len(matches[idx])-1):
                if matches[idx][idx2][1] > matches[idx][max_idx][1]:
                    max_idx = idx2
                else:
                    for elem in range(len(matches)):
                        for elem2 in range(len(matches[elem])):
                            if matches[elem][elem2] == matches[idx][idx2]:
                                matches.remove(matches[elem][elem2])

print(matches)



for idx in range(len(verified_cols) - 1, 0, -1):
    if type(verified_cols[idx]) == list and len(verified_cols[idx]) == 2:
        batch2.rename(columns={verified_cols[idx][1]: verified_cols[idx][0]})
    else:
        break

try:
    for col in df1_cols:
        del batch1[col]
        
    for col in df2_cols:
        del batch2[col]
except: pass
    
"""print(len(batch1.columns))
print(batch1.columns)
print(len(batch2.columns))
print(batch2.columns, "\n")
print(df1_cols)
print(df2_cols)"""

for col in batch1.columns:
    if col not in batch2.columns:
        df1_cols.append(col)
        del batch1[col]
        
for col in batch2.columns:
    if col not in batch1.columns:
        df2_cols.append(col)
        del batch2[col]
        
print(df1_cols)
print(df2_cols)

        

