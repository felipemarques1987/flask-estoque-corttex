from flask import Flask, render_template
import pyodbc
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Conexão com Azure SQL via variáveis de ambiente
conn_str = (
    "Driver={ODBC Driver 17 for SQL Server};"
    f"Server={os.getenv('SQL_SERVER')};"
    f"Database={os.getenv('SQL_DATABASE')};"
    f"Uid={os.getenv('SQL_USER')};"
    f"Pwd={os.getenv('SQL_PASSWORD')};"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)

@app.route("/")
def index():
    query = "SELECT Produto, estoque_atual FROM dbo.PRODUTOS_ESTOQUE_CORTTEX"
    conn = pyodbc.connect(conn_str)
    df = pd.read_sql(query, conn)
    conn.close()
    return render_template("index.html", data=df.to_dict(orient="records"))
