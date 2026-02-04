import pandas as pd

df = pd.DataFrame({"t_kedatangan" : [-5,0,3,7,10,10,-2,5,12,0]})
print(df) 

print('Variasi : ', df.var())
print("STD : ", df.std())
print(df.describe())