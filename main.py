from fastapi import FastAPI
import pyodbc
import os

app = FastAPI()

# Conexão usando variáveis de ambiente do Railway
conn_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={os.getenv('SERVER')},{os.getenv('PORT')};"
    f"DATABASE={os.getenv('DATABASE')};"
    f"UID={os.getenv('UID')};"
    f"PWD={os.getenv('PWD')};"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

def get_conn():
    return pyodbc.connect(conn_str)

@app.post("/orderdetails")
async def create_orderdetail(data: dict):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO OrderDetailsRaw (json_data) VALUES (?)",
        (str(data),)
    )
    conn.commit()

    return {"status": "OK", "message": "OrderDetail recebido com sucesso"}
