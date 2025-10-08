# config.py
# --- Configurações do projeto ---

# ==============================
# 🔑 CONFIGURAÇÕES DA API
# ==============================

# Chave da ScraperAPI (usada para coletar os dados de preços)
API_KEY = "49f0ed352f36f401c18af736c682c4a4"


# ==============================
# 📧 CONFIGURAÇÕES DE E-MAIL
# ==============================

# E-mail remetente (precisa ser o mesmo usado para gerar a senha de app)
EMAIL = "varejotcc@gmail.com"

# Senha de app do Gmail (nunca usar a senha normal da conta!)
SENHA = "vwwx tewa uwpi fzwf"


# ==============================
# ⚙️ OUTRAS CONFIGURAÇÕES
# ==============================

# Nome do arquivo que contém os e-mails de destino
EMAILS_EXCEL = "emails.xlsx"

# Pasta onde os relatórios gerados serão salvos
PASTA_RELATORIOS = "relatorios/"

# Pasta onde o histórico (CSV) será armazenado
PASTA_DADOS = "dados_historicos/"


# ==============================
# ⚠️ IMPORTANTE
# ==============================
# Nunca versionar este arquivo no GitHub!
# Garanta que o .gitignore contenha a linha:
# config.py
