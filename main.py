from fastapi import FastAPI
import pyodbc

app = FastAPI()

# CONFIGURAÇÃO DO SQL SERVER (depois você troca pelos dados do Railway)
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=SEU_SERVIDOR;"
    "DATABASE=SEU_BANCO;"
    "UID=SEU_USUARIO;"
    "PWD=SUA_SENHA;"
)

def get_conn():
    return pyodbc.connect(conn_str)

@app.post("/orderdetails")
async def create_orderdetail(data: dict):
    conn = get_conn()
    cursor = conn.cursor()

    # Insere tudo como JSON bruto em uma tabela temporária (mais simples para começar)
    cursor.execute(
        "INSERT INTO OrderDetailsRaw (json_data) VALUES (?)",
        (str(data),)
    )
    conn.commit()

    return {"status": "OK", "message": "Recebido com sucesso"}