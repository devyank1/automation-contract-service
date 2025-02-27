import time

import yagmail
import os
import pandas as pd

# E-mail configuration
SENDER_EMAIL = "yancarlostrab@gmail.com"
PASSWORD = os.getenv("EMAIL_APP_PASSWORD")

# Create connection with e-mail server
yag = yagmail.SMTP(SENDER_EMAIL, PASSWORD)

# Folder when the contracts are saved
FOLDER_SAVED = "contracts"

# Load client list (Excel)
df = pd.read_excel("clients.xlsx")

# Send contracts for any client
for _, client in df.iterrows():
    client_name = client['Nome'].strip().replace(' ', '_')

    print(f"🔍 Processando cliente: {client_name}")

    files_to_send = [
        os.path.join(FOLDER_SAVED, f)
        for f in os.listdir(FOLDER_SAVED)
        if f.startswith(f"contract_{client_name}") and f.endswith(".docx")
    ]

    print(f"📂 Arquivos encontrados para {client_name}: {files_to_send}")

    if files_to_send:
        subject = "Contrato de Prestação de Serviços"
        body = f"Olá {client['Nome']}, segue anexo seu contrato para assinatura."

        print(f"📧 Enviando e-mail para {client['E-mail']}")

        yag.send(to=client["E-mail"], subject=subject, contents=body, attachments=files_to_send)
        print(f"E-mail send to {client['Nome']} ({client['E-mail']}) com {len(files_to_send)} contrato(s).")

        time.sleep(5)

    else:
        print(f"File not found for {client['Nome']}")

print("All contracts are sent!")