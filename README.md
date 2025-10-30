# 🤖 Chatbot do Kronos

**Autores:** Giovanna Pelati, Júlia Penna, Dmitri Kogake e Theo Correia  
**Turma:** 2°I

---

## 🧩 Descrição do Projeto
O **Chatbot do Kronos** é um assistente virtual integrado ao aplicativo **Kronos**, sistema de gerenciamento de tarefas fabris.  
Seu objetivo é **guiar usuários**, responder dúvidas e manter interações seguras e contextuais.

---

## 🛠 Tecnologias Utilizadas

| Tecnologia | Função |
|-------------|--------|
| **gemini-2.0 / 2.5-flash** | Geração e moderação de respostas |
| **LangChain** | Orquestração dos agentes |
| **gemini-embedding-001** | Criação de embeddings (RAG) |
| **MongoDB** | Armazenamento de histórico e base de conhecimento |
| **FastAPI + Render** | API e hospedagem |

---

## ⚙️ Arquitetura

O sistema é composto por **três agentes**:

| Agente | Função | Modelo |
|--------|---------|--------|
| **Guardrail** | Filtra perguntas inapropriadas | gemini-2.0-flash |
| **Escritor** | Gera respostas com base em contexto (RAG) | gemini-2.5-flash |
| **Juiz** | Revisa e corrige respostas | gemini-2.0-flash |

Fluxo:
1. Usuário envia uma pergunta.  
2. Guardrail valida.  
3. Escritor gera resposta.  
4. Juiz revisa e envia ao usuário.

---

## 💬 Exemplos

| Pergunta | Resposta |
|-----------|-----------|
| Como desatribuir uma tarefa? | Clique no ícone ⚠ da tarefa para reportá-la ao gestor. |
| Como justificar ausência? | Vá ao calendário 🗓 e anexe o arquivo ao registrar a ausência. |
| Como funciona a análise GUT? | Avalia tarefas por gravidade, urgência e tendência (1–5). |

---

## 🗂 Estrutura do Projeto

/kronos-chatbot

├── agents/ # Lógica dos agentes e prompts

├── db_scripts/ # Banco de dados e embeddings

├── services/ # RAG e memória de sessão

├── tests/ # Testes automatizados

├── docs/ # Documentação e imagens

├── pipeline.py # Execução da pipeline

└── main.py # API principal (FastAPI)

## ⚙️ Instalação e Execução

### 1. Clone o repositório
git clone https://github.com/Systems-Kronos/kronos-chatbot.git
cd kronos-chatbot

### 2. Instale as dependências
pip install -r requirements.txt

### 3. Configure as variáveis de ambiente
Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:

GEMINI_API_KEY=coloque_sua_chave_aqui
MONGO_CONNECTION_STRING=sua_connection_string_aqui

### 4. Execute o servidor FastAPI
uvicorn main:app --reload
Acesse em: http://localhost:8000

## 📄 Licença
Este projeto está licenciado sob a licença MIT — veja o arquivo LICENSE para mais detalhes.