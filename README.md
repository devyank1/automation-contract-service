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
<h2 align="center"> ❓ Problemas que o projeto resolve ❓</h2>
1️⃣ Empresas que precisam enviar contratos para clientes, parceiros ou fornecedores fazem isso manualmente. <br>
- O responsável precisa: <br>
1. Abrir o contrato individualmente. <br>
2. Anexar ao e-mail. <br>
3. Escrever a mensagem e enviar e repetir o processo, sujeito a erros humanos. <br> <br>

2️⃣ Risco de Esquecer ou Enviar para o Destinatário Errado <br>
- Em processos manuais, erros humanos são comuns: <br>
1. Enviar um contrato para o cliente errado. <br>
2. Esquecer de enviar um contrato para um cliente importante. <br>
3. Deixar passar contratos pendentes, gerando atrasos. <br>

3️⃣ Falta de Monitoramento dos Envios
- Depois de enviar contratos manualmente, a empresa não tem controle sobre:
1. Quem recebeu o contrato e quem não recebeu.
2. E-mails inválidos ou que falharam no envio.
3. Rastreamento dos contratos enviados.

<h2 align="center"> ✅ Soluções para os problemas ✅</h2> 
- O código automatiza o envio de contratos <br>
- Aumento de produtividade, já que o funcionário não precisa enviar manualmente cada contrato. <br>
- O código lê automaticamente os dados corretos do cliente no Excel. <br>
- Mais segurança e rastreabilidade, evitando erros no envio. <br>
- Caso um e-mail falhe, o responsável recebe uma notificação e pode corrigir rapidamente. <br>
- Transparência e rastreabilidade no processo, evitando falhas de comunicação. <br>

<h2 align="center"> 🔎 Para Quais Empresas Esse Projeto é Útil? 🔎</h2>
✅ Escritórios de Contabilidade (envio automatizado de contratos para clientes e parceiros) <br>
✅ Empresas de Serviços (advocacia, RH terceirizado, consultorias) <br>
✅ Empresas de Tecnologia (contratos de prestação de serviço com clientes) <br>
✅ Imobiliárias (envio de contratos de aluguel ou compra de imóveis) <br>
✅ Departamentos Jurídicos (gestão e envio de documentos para clientes) <br>
✅ Startups (processos de onboarding de clientes automatizados) <br>
