INSTRUÇÕES DE DEPLOY NO RENDER.COM

1. Acesse https://render.com e crie uma conta (ou faça login).

2. No dashboard, clique em "New" > "Web Service".

3. Conecte ao seu repositório Git com este projeto.

4. Preencha:
   - Name: flask-estoque-corttex
   - Runtime: Python 3
   - Build Command: pip install -r requirements.txt
   - Start Command: gunicorn app:app

5. Configure as variáveis de ambiente:
   - SQL_SERVER
   - SQL_DATABASE
   - SQL_USER
   - SQL_PASSWORD

6. Clique em "Create Web Service" e aguarde o deploy.

Após isso, o app estará disponível em um link como:
https://flask-estoque-corttex.onrender.com/

OBS:
- Este projeto exibe os dados da view dbo.PRODUTOS_ESTOQUE_CORTTEX de forma pública.
- O usuário SQL tem acesso restrito somente a essa view.
