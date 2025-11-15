# 🚀 Etapa 1 — Reforço de Arquitetura (MVC + Banco) + Roadmap e Kanban

## 🎯 Objetivo
Criar a base do sistema logístico, começando com **cadastro de motoristas e veículos**, utilizando a arquitetura **MVC (Model–View–Controller)**, **CustomTkinter**, **PostgreSQL/MySQL** e boas práticas de organização.

---

# 📦 PARTE 1 — ARQUITETURA E FUNDAMENTOS

## 🧱 1. Estrutura de Pastas

```
sistema_transporte/
│
├── main.py
│
├── model/
│   ├── motorista.py
│   ├── veiculo.py
│   └── database.py
│
├── view/
│   ├── janela_principal.py
│   ├── form_motorista.py
│   └── form_veiculo.py
│
└── controller/
    ├── motorista_controller.py
    └── veiculo_controller.py
```

### 🧩 Explicação da Estrutura
- **model/** → Banco de dados e regras de negócio.  
- **view/** → Interfaces gráficas (CustomTkinter).  
- **controller/** → Intermediação entre interface e regras.  
- **main.py** → Ponto de entrada da aplicação.

---

## 🗂️ 2. Planejamento das Entidades

### Entidade: Motorista
| Campo | Tipo | Observação |
|--------|------|------------|
| id_motorista | INT | PK, autoincremento |
| nome | VARCHAR(100) | obrigatório |
| cpf | VARCHAR(14) | único |
| telefone | VARCHAR(15) | opcional |
| cnh | VARCHAR(15) | obrigatório |

---

### Entidade: Veículo
| Campo | Tipo | Observação |
|--------|------|------------|
| id_veiculo | INT | PK, autoincremento |
| placa | VARCHAR(8) | único |
| modelo | VARCHAR(50) | obrigatório |
| ano | INT | opcional |
| id_motorista | INT | FK → motorista.id_motorista |

🧠 **Observação:** Um motorista pode dirigir vários veículos (1:N).

---

## ⚙️ 3. Banco de Dados

### Banco recomendado:
- **PostgreSQL** (projetos reais)  
- **SQLite** (protótipo rápido local)

### Tarefas

**FAZER**  
- Criar conexão (`database.py`).  
- Criar tabelas `motorista` e `veiculo` (Postgres).  

**FAZENDO**  
- Criar funções de manipulação.

**FEITO**  
- —  

---

## 🧠 4. Model (Regras de Negócio)

Em cada classe (motorista.py e veiculo.py):

- Atributos correspondentes ao banco.  
- Construtor.  
- Validações:  
  - CPF válido  
  - Placa única  
  - CNH obrigatória  

O model **não acessa banco diretamente**.

---

## 🧩 5. Controller (Lógica e Conexão)

Responsável por:

- Receber dados da view  
- Validar  
- Executar operações no banco  
- Retornar mensagem ou status  

### Tarefas:

**FAZER**  
- CRUD completo.  
- Função de busca.  
- Retorno padronizado (bool/msg).  

**FAZENDO**  
- —  

**FEITO**  
- —  

---

## 🪟 6. View (Interface CustomTkinter)

Arquivos:
- `janela_principal.py` → menu e navegação  
- `form_motorista.py` → cadastro/edição  
- `form_veiculo.py` → cadastro/edição  

Regras:

- Nada de SQL na view.  
- Apenas pegar dados dos inputs e chamar controllers.  
- Treeview para listagem.

---

## 🧩 7. main.py (Ponto de Entrada)

O main deve:

1. Conectar ao banco  
2. Criar tabelas  
3. Iniciar janela principal  

Sem regras de negócio.

---

## 🔄 8. Teste da Arquitetura

Antes da interface:

- Testar controller → model → database no terminal.  
- Simular cadastros.  
- Testar exceções.  

Depois:

- Integrar com CustomTkinter.  
- Testar botões.  
- Testar atualização automática do Treeview.

---

## 📋 9. Entrega da Etapa

**Resultados esperados:**

- Estrutura MVC criada  
- Banco funcionando  
- CRUD de motoristas e veículos  
- Conexão 100% separada  
- Sem lógica misturada na interface  

---

# 📌 PARTE 2 — ROADMAP GERAL DO SISTEMA LOGÍSTICO

## 🟦 BACKLOG
- Dashboard com estatísticas  
- Cadastro de Cargas  
- Cadastro de Viagens  
- Workflow logístico (saída, chegada, finalização)  
- Relatórios PDF  
- Login + Níveis de usuário  
- Logs de auditoria  
- Exportar para Excel  
- API REST (FastAPI/Flask)  

---

## 🟩 A FAZER (Sprint Atual)
- Criar sistema MVC base  
- Criar model e controller de motorista  
- Criar model e controller de veículo  
- Criar banco + tabelas no PostgreSQL  
- Criar Views de Motorista e Veículo  
- Integrar Controller ↔ View  
- Testes locais  
- Validar dados  

---

## 🟧 FAZENDO
- Integrando Interface  
- Testando CRUD  
- Validando campos  

---

## 🟨 FEITO
*(Mover conforme concluir)*

---

# 🗂️ Kanban sugerido

```
📋 A FAZER
- Montar estrutura de pastas
- Criar database.py
- Criar tabelas no PostgreSQL
- Criar classes Motorista e Veiculo
- Criar controllers
- Criar interface básica
- Testar integração

⚙️ EM PROGRESSO
- CRUD Motorista
- CRUD Veículo

✅ CONCLUÍDO
(Deixe em branco para ir preenchendo)
```

---

# 🌟 Conclusão

Este arquivo reúne:

- Arquitetura MVC  
- Planejamento das entidades  
- Etapas da implementação  
- Roadmap completo  
- Kanban pronto para uso  
- Objetivos da Etapa 1  
- Organização profissional de projeto  