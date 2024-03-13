from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx
import mysql.connector

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# GET 요청이 오면 {"Hello": "World"}를 JSON 형태로 반환
@app.get("/")
async def read_root() :
    return {"Hello" : "World"}

@app.get("/table")
async def get_table_names():
    url = "http://localhost:8001/table"
    response = httpx.get(url)
    response.raise_for_status()  # 오류 발생 시 예외를 일으킴
    table_names = response.json()  # JSON 데이터 추출
    return {"8001 요청": table_names}
