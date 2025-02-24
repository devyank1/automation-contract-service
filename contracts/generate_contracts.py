import pandas as pd
from docxtpl import DocxTemplate
import os

# Define paths
TEMPLATE_PATH = os.path.join(os.getcwd(), "..", "template", "contract.docx")
CONTRACT_FOLDER = "contracts"
EXCEL_CLIENTS = "clients.xlsx"

# Create a folder to save contracts, if it does not exist.
if not os.path.exists(CONTRACT_FOLDER):
    os.makedirs(CONTRACT_FOLDER)

# Load the clients list (Excel)
df = pd.read_excel(EXCEL_CLIENTS)

# Generate contracts for any client
for _, client in df.iterrows():
    doc = DocxTemplate(TEMPLATE_PATH)

    # Create a dictionary with client data
    context = {
        "empresa": client["Empresa"],
        "cnpj": client["CNPJ"],
        "endereco_empresa": client["Endereço Empresa"],
        "cliente": client["Nome"],
        "cpf": client["CPF"],
        "endereco_cliente": client["Endereço Cliente"],
        "descrição_servico": client["Serviço"],
        "data_inicio": client["Data Início"],
        "data_fim": client["Data Fim"],
        "valor": f"R$ {client['Valor']:.2f}",
        "forma_pagamento": client["Forma Pagamento"],
        "representante_empresa": "Carlos Almeida",
        "cidade": "São Paulo",
        "data": "24/02/2024"
    }

    # Rendering a contract with all clients data
    doc.render(context)

    # Saved file name
    file_name = f"contract_{client['Nome'].replace(' ', '_')}.docx"
    file_path = os.path.join(CONTRACT_FOLDER, file_name)
    doc.save(file_path)

    print(f"Contract generated {file_path}")

print("\n All contracts successfully generated")

df["Status"] = "Pendente Assinatura"
df.to_excel("relatorio_contratos.xlsx", index=False)

print("Relatory saved: relatories_contract.xlsx")