import pandas as pd

file_path = "Transaction.csv"

total_records = 0
running_sum = 0

for chunk in pd.read_csv(file_path, chunksize=10000):

    total_records += len(chunk)

    running_sum += chunk["Amount"].sum()

if total_records > 0:
    average_transaction = running_sum / total_records
else:
    average_transaction = 0

print("Total Records:", total_records)
print("Total Transaction Amount:", running_sum)
print("Average Transaction Value:", average_transaction)