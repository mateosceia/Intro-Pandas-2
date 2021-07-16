import pandas as pd
df = pd.DataFrame({1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]})

def columna(df, columna):
    presente = columna in df.columns
    return("La columna " + str(columna) + " esta en el Dataframe?: " + str(presente))
print(columna(df,1)) 

print(columna(df,"A"))
