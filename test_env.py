from dotenv import load_dotenv
import os, json

load_dotenv()

raw = os.getenv("GOOGLE_CREDENTIALS_JSON")
if not raw:
    print("❌ Variável GOOGLE_CREDENTIALS_JSON não encontrada!")
    exit()

print("✅ Variável encontrada! Tamanho:", len(raw))

try:
    data = json.loads(raw)
    print("✅ JSON válido!")
    print("🔹 Campos encontrados:", list(data.keys()))
    print("🔹 Email da conta de serviço:", data.get("client_email"))
except Exception as e:
    print("❌ Erro ao decodificar JSON:", e)
