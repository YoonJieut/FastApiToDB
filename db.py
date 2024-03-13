from fastapi import FastAPI
import uvicorn
from db.config import db_config
import mysql.connector


mydb = mysql.connector.connect(
    host=db_config.host,
    port=db_config.port,
    user=db_config.user,
    password=db_config.password,
    database=db_config.database
)

app = FastAPI()

@app.get('/')
async def read_root():
    return {"Hello": "im 8001"}

# 테이블 이름 가져오기
@app.get("/table")
async def get_table_names():
    cursor = mydb.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    table_names = [table[0] for table in tables]
    return {"tables": table_names}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
