import pandas as pd


#Tabela de conversão
grade_map = {
    'A+': 4.0,
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'F': 0.0
}



#Lê o arquivo CSV
dados = pd.read_csv("data/raw/Grades.csv")

cols_grade = dados.columns[1:-1]

#Aplicando o mapeamento das notas
for col in cols_grade:
    dados[col] = dados[col].map(grade_map)

#Salvar dados tratados
dados.to_csv("data/processed/grades_numeric.csv", index=False)










#Calcula a média da coluna CGPA

media_cgpa = dados['CGPA'].mean()
media_cgpa = round(media_cgpa, 3)
print("Média CGPA CS", media_cgpa)