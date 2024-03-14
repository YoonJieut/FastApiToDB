import React, { useState, ChangeEvent } from "react";
import axios from "axios";

const UploadImage = () => {
  const [image, setImage] = useState<File | null>(null);

  const handleImageChange = (event: ChangeEvent<HTMLInputElement>) => {
    if (event.target.files && event.target.files.length > 0) {
      setImage(event.target.files[0]);
    }
  };

  const handleImageUpload = async () => {
    try {
      if (!image) {
        console.error("No image selected");
        return;
      }
      console.log("Uploading image:", image);
      const formData = new FormData();
      formData.append("image", image);

      // 이미지를 업로드하는 API 엔드포인트 URL
      const apiUrl = "http://localhost:8000/upload-image";

      // POST 요청을 사용하여 이미지를 업로드하는 API 엔드포인트로 FormData 객체 전송
      const response = await axios.post(apiUrl, formData);

      console.log("Image uploaded successfully:", response.data);
    } catch (error) {
      console.error("Error uploading image:", error);
    }
  };

  return (
    <div>
      <h2>이미지 업로드</h2>
      <input type="file" accept="image/*" onChange={handleImageChange} />
      <button onClick={handleImageUpload}>이미지 업로드</button>
    </div>
  );
};

export default UploadImage;
