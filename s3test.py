import boto3

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
