# enviar_email.py
import yagmail
import pandas as pd
from config import EMAIL, SENHA

def enviar_relatorio(relatorio_path):
    # --- Lê os destinatários do Excel ---
    try:
        df = pd.read_excel("emails.xlsx")
        destinatarios = df["email"].dropna().tolist()
    except Exception as e:
        print("Erro ao ler emails.xlsx:", e)
        return

    if not destinatarios:
        print("Nenhum destinatário encontrado no emails.xlsx")
        return

    # --- Configura o Yagmail ---
    try:
        yag = yagmail.SMTP(EMAIL, SENHA)
    except Exception as e:
        print("Erro ao conectar no e-mail:", e)
        return

    # --- Envia o e-mail ---
    assunto = "Relatório de Preços - TCC"
    conteudo = f"Segue em anexo o relatório gerado.\n\nAtenciosamente,\nSistema TCC"
    try:
        yag.send(to=destinatarios, subject=assunto, contents=conteudo, attachments=relatorio_path)
        print(f"Relatório enviado com sucesso para: {', '.join(destinatarios)}")
    except Exception as e:
        print("Erro ao enviar e-mail:", e)

# --- Teste rápido ---
if __name__ == "__main__":
    # Substitua pelo caminho de um relatório existente
    enviar_relatorio("relatorios/relatorio_20250909_193012.txt")
