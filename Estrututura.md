# 🚀 Etapa 1 — Reforço de Arquitetura (MVC + Banco)

## 🎯 Objetivo
Criar a base do sistema logístico, começando com **cadastro de motoristas e veículos**, utilizando a arquitetura **MVC (Model–View–Controller)** e **CustomTkinter + Banco de Dados**.

---

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
- **model/** → Tudo relacionado ao **banco de dados e regras de negócio.**
- **view/** → As **interfaces gráficas** (CustomTkinter).
- **controller/** → Camada intermediária que **liga a view ao model.**
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

### Entidade: Veículo
| Campo | Tipo | Observação |
|--------|------|------------|
| id_veiculo | INT | PK, autoincremento |
| placa | VARCHAR(8) | único |
| modelo | VARCHAR(50) | obrigatório |
| ano | INT | opcional |
| id_motorista | INT | FK → motorista.id_motorista |

🧠 **Dica:** Um motorista pode dirigir vários veículos (relação 1:N).

---

## ⚙️ 3. Banco de Dados

### Decisão
Use **MySQL** se quiser algo profissional e escalável, ou **SQLite3** se quiser praticidade local.


## KANBAN

**FAZER**
**FAZENDO**
**FEITO**
- Criar conexão (`database.py`).
- Criar tabelas `motorista` e `veiculo`. (postgree)
- Criar tabelas `motorista` e `veiculo`. (python)
- Implementar funções: `conectar()`, `criar_tabelas()`, `executar_comando()`, `consultar_dados()` (será feito direto na query postgres por enquanto)
---

## 🧠 4. Model (Regras de Negócio)

Cada arquivo (`motorista.py`, `veiculo.py`) deve conter uma classe com:
- Atributos.
- Construtor.
- Validações e métodos auxiliares.

📘 O model **não conhece a interface**, apenas as regras (ex: validação de CPF, placa única, etc.).

---

## 🧩 5. Controller (Lógica e Conexão)

Responsável por:
- Receber dados da view.
- Validar com o model.
- Enviar comandos ao banco.

Deve conter:
- CRUD completo.
- Função de busca.
- Retorno padronizado (True/False ou mensagens).

🧠 Dica: Nenhum SQL dentro da view.

**FAZER**
**FAZENDO**
**FEITO**
- CRUD completo.
- Função de busca.
- Retorno padronizado (True/False ou mensagens).
---

## 🪟 6. View (Interface CustomTkinter)

As views devem:
- Mostrar formulários e botões.
- Coletar dados do usuário.
- Enviar para o controller.

Arquivos:
- `janela_principal.py`: tela principal.
- `form_motorista.py`: formulário de motorista.
- `form_veiculo.py`: formulário de veículo.

Regra: **Nada de SQL ou lógica aqui** — apenas interface e chamadas para o controller.

---

## 🧩 7. main.py (Ponto de Entrada)

Responsável por:
1. Conectar ao banco.
2. Criar tabelas.
3. Iniciar a janela principal.

Nada de regras de negócio aqui.

---

## 🔄 8. Teste da Arquitetura

Antes de criar a interface:
- Teste controller → model → database.
- Faça simulações no terminal.
- Verifique criação das tabelas.

Depois:
- Conecte com CustomTkinter.
- Teste botões e Treeview.

---

## 📋 9. Entrega da Etapa

**Resultados esperados:**
- Estrutura MVC completa.
- Banco funcional.
- CRUD de motoristas e veículos (sem interface complexa).
- Conexão e camadas separadas.

---

## 💡 Dica para Kanban
Crie colunas como:
- 📋 A Fazer
- ⚙️ Em Progresso
- ✅ Concluído

E adicione cartões para:
1. Criar estrutura de pastas.  
2. Configurar banco e tabelas.  
3. Criar classes de modelo.  
4. Implementar controladores.  
5. Montar interface básica.  
6. Testar integração completa.