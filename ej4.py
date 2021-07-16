import pandas as pd
df = pd.DataFrame({1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]})
def borrar(df, fila):
    df2 = df.iloc[fila:]
    return df2
print(df)
print(borrar(df,3))