from flask import Flask, render_template
import pymssql
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Conexão com Azure SQL via variáveis de ambiente


conn = pymssql.connect(
    server=os.getenv("SQL_SERVER"),
    user=os.getenv("SQL_USER"),
    password=os.getenv("SQL_PASSWORD"),
    database=os.getenv("SQL_DATABASE"),
    port=1433
)

@app.route("/")
def index():
    query = "SELECT Produto, estoque_atual FROM dbo.PRODUTOS_ESTOQUE_CORTTEX"
    conn = pyodbc.connect(conn_str)
    df = pd.read_sql(query, conn)
    conn.close()
    return render_template("index.html", data=df.to_dict(orient="records"))
