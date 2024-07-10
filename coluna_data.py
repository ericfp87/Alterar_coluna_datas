import pandas as pd

# Carregue o arquivo csv
df = pd.read_csv(r'V:\10 - NÉXIA\Eric\teste\indicadores_leitura_old2.csv', delimiter=";")


# Certifique-se de que a coluna 'REFER' é do tipo datetime
df['REFER'] = pd.to_datetime(df['REFER'], format='%d/%m/%Y %H:%M')

# Crie a nova coluna 'REFER2' no formato YYYYMM
df['REFER2'] = df['REFER'].dt.strftime('%Y%m')

#df2 = df[['REFER2','UNIDADE','GERENCIA','QTD_LEITURAS','COD_OCORRENCIA']]

# Salve o dataframe de volta para um arquivo csv
df.to_csv(r'V:\10 - NÉXIA\Eric\teste\seu_arquivo_atualizado_conferir.csv', index=False)

print("Concluído")
