import pandas as pd
d1 = {1:[1,2,3], 2:[4,5,6], 3:[7,8,9]}
df = pd.DataFrame(d1)
print(df)

lista = ["a", "b", "c"]
def add_list(lista, nombre, df):
    serie = pd.Series(lista, name=nombre)
    return pd.concat([df,serie], axis=1)
print(add_list(lista, 4, df))