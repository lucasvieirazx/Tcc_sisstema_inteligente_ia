# main.py
import requests
import pandas as pd
import matplotlib.pyplot as plt
import schedule
import time
import yagmail
from config import API_KEY

# ================================
# Funções principais
# ================================

def coletar_clima(cidade: str):
    """Coleta dados climáticos atuais de uma cidade usando a API OpenWeatherMap."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        return {
            "cidade": cidade,
            "descricao": dados['weather'][0]['description'],
            "temperatura": dados['main']['temp'],
            "vento": dados['wind']['speed'],
            "umidade": dados['main']['humidity']
        }
    else:
        print("Erro ao coletar clima:", resposta.status_code)
        return None

def coletar_mare(local: str, data: str):
    """Simula a coleta de dados de maré (aqui depois você vai integrar API ou PDF da Marinha)."""
    # Exemplo fictício por enquanto
    return {
        "local": local,
        "data": data,
        "mare_alta": 2.1,
        "mare_baixa": 0.5
    }

def analisar_condicoes(clima: dict, mare: dict):
    """Analisa as condições e retorna se é favorável para atracação."""
    if not clima or not mare:
        return "Dados insuficientes para análise."
    
    regras = []
    if 1.5 <= mare["mare_alta"] <= 2.5:
        regras.append("✅ Maré dentro do ideal (1.5–2.5 m)")
    else:
        regras.append("⚠️ Maré fora do ideal")

    if clima["vento"] < 20:
        regras.append("✅ Vento abaixo de 20 km/h")
    else:
        regras.append("⚠️ Vento forte")

    if "chuva" not in clima["descricao"].lower():
        regras.append("✅ Sem chuvas fortes")
    else:
        regras.append("⚠️ Chuva detectada")

    return regras

def gerar_relatorio(clima: dict, mare: dict, analise: list):
    """Gera um relatório simples em texto."""
    relatorio = f"""
    ===== Relatório de Condições =====
    Local: {clima['cidade']}
    Temperatura: {clima['temperatura']} °C
    Condição: {clima['descricao']}
    Vento: {clima['vento']} km/h
    Umidade: {clima['umidade']} %

    Maré Alta: {mare['mare_alta']} m
    Maré Baixa: {mare['mare_baixa']} m

    --- Análise ---
    """
    for regra in analise:
        relatorio += f"\n- {regra}"

    return relatorio

def enviar_email(destinatarios: list, assunto: str, conteudo: str):
    """Envia relatório por e-mail usando yagmail."""
    try:
        yag = yagmail.SMTP("SEU_EMAIL_AQUI", "SENHA_APP_AQUI")  # Config no config.py depois
        yag.send(to=destinatarios, subject=assunto, contents=conteudo)
        print("✅ Email enviado com sucesso!")
    except Exception as e:
        print("Erro ao enviar email:", e)

# ================================
# Execução principal
# ================================
if __name__ == "__main__":
    cidade = "Rio de Janeiro"
    data = "2025-08-18"

    clima = coletar_clima(cidade)
    mare = coletar_mare(cidade, data)
    analise = analisar_condicoes(clima, mare)
    relatorio = gerar_relatorio(clima, mare, analise)

    print(relatorio)

    # Exemplo de envio (coloque seus emails)
    # enviar_email(["destinatario@gmail.com"], "Relatório Clima e Maré", relatorio)