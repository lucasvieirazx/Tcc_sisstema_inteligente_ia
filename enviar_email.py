# enviar_email.py
import smtplib
from email.message import EmailMessage
from config import EMAIL, SENHA
import openpyxl
import os

def carregar_destinatarios():
    """Lê os e-mails do arquivo emails.xlsx"""
    arquivo = "emails.xlsx"
    if not os.path.exists(arquivo):
        print("⚠️ Arquivo emails.xlsx não encontrado. Nenhum e-mail será enviado.")
        return []

    planilha = openpyxl.load_workbook(arquivo)
    aba = planilha.active
    emails = []

    for linha in aba.iter_rows(min_row=2, values_only=True):
        if linha[0]:
            emails.append(linha[0])
    return emails

def enviar_relatorio():
    """Envia o relatório TXT por e-mail para os destinatários"""
    destinatarios = carregar_destinatarios()
    if not destinatarios:
        print("⚠️ Nenhum destinatário encontrado.")
        return

    caminho_relatorio = "relatorios/relatorio_atual.txt"
    if not os.path.exists(caminho_relatorio):
        print("⚠️ Relatório não encontrado. Gere o relatório antes de enviar.")
        return

    # Lê o conteúdo do relatório
    with open(caminho_relatorio, "r", encoding="utf-8") as f:
        conteudo = f.read()

    # Cria o e-mail
    msg = EmailMessage()
    msg["Subject"] = "Relatório de Preços - Notebooks e Hardware"
    msg["From"] = EMAIL
    msg["To"] = ", ".join(destinatarios)
    msg.set_content(conteudo)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL, SENHA)
            smtp.send_message(msg)
            print(f"✅ E-mail enviado com sucesso para: {', '.join(destinatarios)}")
    except Exception as e:
        print(f"❌ Erro ao enviar e-mail: {e}")
