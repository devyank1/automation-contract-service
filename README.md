<h1 align = "center">📩 Sistema de Envio de Contratos Automático</h1>

Este projeto automatiza o envio de contratos via e-mail, utilizando Python, Pandas e Yagmail.

## 🚀 Funcionalidades
✅ Envia contratos automaticamente com base em um Excel <br>
✅ Gera logs de envios bem-sucedidos e falhas <br>
✅ Pode ser integrado a um frontend ou API <br>

## 🛠 Tecnologias usadas
- Python
- Pandas
- Yagmail

## 📌 Como rodar?
1. Clone o repositório:
   ```sh
   git clone https://github.com/devyank1/automation-contract-service.git
2. Instale as dependências:
   ```sh
   pip install -r requirements.txt
3. Configure sua senha de E-mail
   ```sh
   export EMAIL_APP_PASSWORD="sua_senha"
4. Execute os scripts:
   ```sh
   python generate_contracts.py
   python send_contracts.py
   ```
<h2 align="center"> Problemas que o projeto resolve</h2>
## Empresas que precisam enviar contratos para clientes, parceiros ou fornecedores fazem isso manualmente.
- O responsável precisa:
1. Abrir o contrato individualmente.
2. Anexar ao e-mail.
3. Escrever a mensagem e enviar e repetir o processo, sujeito a erros humanos.
