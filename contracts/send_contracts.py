import yagmail
import os
import pandas as pd

# E-mail configuration
SENDER_EMAIL = "youremail@gmail.com"
PASSWORD = "your_password"

# Create connection with e-mail server
yag = yagmail.SMTP(SENDER_EMAIL, PASSWORD)

# Folder when the contracts are saved
FOLDER_SAVED = "contracts"

# Load client list (Excel)
df = pd.read_excel("clients.xlsx")

# Send contracts for any client
for _, client in df.iterrows():
    file_name = f"contrato_{client['Nome'].replace(' ', '_')}.docx"
    file_path = os.path.join(FOLDER_SAVED, file_name)

    if os.path.exists(file_path):
        subject = "Contrato de Prestação de Serviços"
        body = f"Olá {client['Nome']}, segue anexo seu contrato para assinatura."

        yag.send(to=client["E-mail"], subject=subject, contents=body, attachments=file_path)
        print(f"E-mail send to {client['Nome']} ({client['E-mail']})")
    else:
        print(f"File not found for {client['Nome']}")

print("All contracts are sent!")