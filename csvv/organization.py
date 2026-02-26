import pandas as pd

df = pd.read_csv(
    "csvv/crimes_violentos_2025.csv",
    sep=";",
    encoding = "utf-8-sig",
    low_memory = False
)
df.columns = df.columns.str.strip().str.lower()

print(df.shape)
print(df.columns.tolist())

df = df.dropna(axis = 1 , how = "all")


coluna_registro = ["registros", "natureza", "municipio", "cod_municipio", "mes", "ano", "risp", "rmbh"]
coluna_registro = [c for c in coluna_registro if c in df.columns]
df_registro = df[coluna_registro]

coluna_location = ["municipio","cod_municipio", "risp", "rmbh"]
colunas_location = [c for c in coluna_location if c in df.columns]
df_location = df[coluna_location]

coluna_crime = ["natureza"]
coluna_crime = [c for c in coluna_crime if c in df.columns]
df_coluna = df[coluna_crime]

print(df_location.head())