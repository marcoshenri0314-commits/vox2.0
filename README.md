# VOX 2.0 — Etapa de conexão

Projeto inicial em Python + Flask com uma rota para testar a resposta da API do Supabase.

## Arquivos
- `app.py`: aplicação Flask e teste de conexão.
- `requirements.txt`: bibliotecas necessárias.
- `ENV_EXAMPLE.txt`: modelo de variáveis de ambiente.
- `GITIGNORE_EXAMPLE.txt`: proteção do arquivo `.env`.
- `README.md`: instruções.

## Quando estiver em um computador
1. Instale Python 3.11 ou superior.
2. Abra um terminal nesta pasta.
3. Crie e ative um ambiente virtual: `python -m venv .venv`
4. Instale as dependências: `pip install -r requirements.txt`
5. Renomeie `ENV_EXAMPLE.txt` para `.env`.
6. Preencha `SUPABASE_URL` com a URL base do projeto (sem `/rest/v1/`).
7. Preencha `SUPABASE_KEY` com a Publishable key (`sb_publishable_...`).
8. Renomeie `GITIGNORE_EXAMPLE.txt` para `.gitignore`.
9. Execute `python app.py`.
10. Teste `http://127.0.0.1:5000/health` e `http://127.0.0.1:5000/health/supabase`.

## Segurança e limites desta etapa
- Nunca use `sb_secret_` ou `service_role` neste arquivo de configuração.
- Nunca envie o arquivo `.env` ao GitHub.
- A rota `/health/supabase` verifica se a API REST do projeto responde; ela não testa permissões de tabelas, políticas RLS nem cadastro/login.
- Esta etapa não cria nem altera tabelas, usuários, buckets ou arquivos no Supabase.
- Cadastro, login e demais funcionalidades ainda não foram implementados.
