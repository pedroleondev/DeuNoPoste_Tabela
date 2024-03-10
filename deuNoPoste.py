import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

data = datetime.now()
fd = data.strftime("%d-%m-%Y %H-%M")


# URL do site
url = 'https://www.ojogodobicho.com/deu_no_poste.htm'

# Fazendo a solicitação para obter o conteúdo da página
response = requests.get(url)

# Analisando o conteúdo HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrando todas as tabelas na página
tables = soup.find_all('table')

# Se houver pelo menos uma tabela
if tables:
    # Pegando a primeira tabela
    first_table = tables[0]

    # Extraindo os dados da tabela
    table_data = []
    for row in first_table.find_all('tr'):
        row_data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
        table_data.append(row_data)

    # Convertendo para DataFrame do pandas
    df = pd.DataFrame(table_data[1:], columns=table_data[0])

    # Salvando como CSV

    df.to_csv(f"tabela-{fd}.csv", index=False)
    df.to_csv('output.csv', index=False)
    print("Tabela extraída e salva.")
else:
    print("Nenhuma tabela encontrada na página.")
