# main.py
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os
from config import API_KEY  # chave ScraperAPI do config.py

# --- Configurações ---
url_produto = "https://lista.mercadolivre.com.br/notebook"

payload = {
    'api_key': API_KEY,
    'url': url_produto
}

# --- Consulta a página via ScraperAPI ---
response = requests.get('https://api.scraperapi.com/', params=payload)

# --- Debug: mostrar status e início do HTML ---
print("Status code:", response.status_code)
print("Início do conteúdo retornado:")
print(response.text[:500])

if response.status_code != 200:
    print("Erro ao acessar a página")
    exit()

# --- Salvar HTML para inspecionar estrutura (temporário) ---
with open("teste.html", "w", encoding="utf-8") as f:
    f.write(response.text)
print("HTML salvo em teste.html para inspeção")

# --- Parse do HTML ---
soup = BeautifulSoup(response.text, "html.parser")

# --- Seletor atualizado para produtos ---
produtos = soup.find_all("li", {"class": "ui-search-layout__item"})

# --- Extrai nome e preço ---
lista_produtos = []
for p in produtos[:10]:  # pega só os 10 primeiros produtos
    nome_tag = p.find("h2", class_="ui-search-item__title")
    preco_tag = p.find("span", class_="price-tag-fraction")
    if nome_tag and preco_tag:
        lista_produtos.append({
            "nome": nome_tag.text.strip(),
            "preco": preco_tag.text.strip()
        })

if not lista_produtos:
    print("Nenhum produto encontrado. Verifique a estrutura do HTML no teste.html")
    exit()

# --- Salva CSV ---
os.makedirs("dados_historicos", exist_ok=True)
data_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
csv_file = f"dados_historicos/produtos_{data_hora}.csv"

with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["nome", "preco"])
    writer.writeheader()
    writer.writerows(lista_produtos)

print(f"Dados salvos em {csv_file}")

# --- Gera relatório TXT ---
os.makedirs("relatorios", exist_ok=True)
txt_file = f"relatorios/relatorio_{data_hora}.txt"

with open(txt_file, "w", encoding="utf-8") as f:
    f.write("Relatório de Preços - TCC\n")
    f.write(f"Data/Hora: {datetime.now()}\n\n")
    for prod in lista_produtos:
        f.write(f"{prod['nome']} - R$ {prod['preco']}\n")

print(f"Relatório salvo em {txt_file}")
