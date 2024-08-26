import csv

dados = [
    ['country', 'currency name', 'continent', 'neighbours'], 
    ['Brazil', 'Real', 'South America', 'Argentina, Paraguay, Uruguay'], 
    ['Germany', 'Euro', 'Europe', 'France, Poland, Denmark'],   
]

with open('dados.csv', mode='w', newline='') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerows(dados)

print("Dados salvos.")
