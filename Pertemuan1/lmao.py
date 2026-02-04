import pandas as pd

data_mahasiswa = pd.read_csv("data.csv")
print(data_mahasiswa.mean(numeric_only=True))
