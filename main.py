from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
import boto3


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


# MariaDB 연결 설정
# 튜플로 작성하면 못 불러온다.
db_config = {
  "host": "127.0.0.1",
  "port": "3306",
  "user": "root",
  "password": "0000",
  "database": "test_database"
}

mydb = mysql.connector.connect(**db_config)

# 테이블 이름 가져오기
@app.get("/table")
async def get_table_names():
    cursor = mydb.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    table_names = [table[0] for table in tables]
    return {"tables": table_names}
  


# S3 객체 업로드
s3 = boto3.client('s3')
s3.upload_file('local_file_path', 'bucket_name', 'object_key')

# 데이터베이스에 이미지 URL 저장
cursor = db_connection.cursor()
cursor.execute("INSERT INTO images (name, file_path) VALUES (%s, %s)", (name, s3_object_url))
db_connection.commit()

# 데이터베이스에서 이미지 URL 불러오기
cursor.execute("SELECT file_path FROM images WHERE id = %s", (image_id,))
result = cursor.fetchone()
image_url = result[0]
