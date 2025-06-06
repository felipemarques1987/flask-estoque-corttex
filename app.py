from flask import Flask, render_template
import pymssql
import pandas as pd
import os
from dotenv import load_dotenv

# Carrega variáveis do .env (para testes locais)
load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    # Conexão com Azure SQL via pymssql
    conn = pymssql.connect(
        server=os.getenv("SQL_SERVER"),
        user=os.getenv("SQL_USER"),
        password=os.getenv("SQL_PASSWORD"),
        database=os.getenv("SQL_DATABASE"),
        port=1433
    )

    # Query na view específica
    query = "SELECT Produto, estoque_atual FROM dbo.PRODUTOS_ESTOQUE_CORTTEX"

    # Lê os dados e fecha a conexão
    df = pd.read_sql(query, conn)
    conn.close()

    # Envia dados para o template
    return render_template("index.html", data=df.to_dict(orient="records"))
