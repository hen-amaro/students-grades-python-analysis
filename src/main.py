import pandas as pd

#Lê o arquivo CSV

dados = pd.read_csv("data/raw/Grades.csv")

#Calcula a média da coluna CGPA

media_cgpa = dados['CGPA'].mean()
media_cgpa = round(media_cgpa, 3)
print("Média CGPA CS", media_cgpa)