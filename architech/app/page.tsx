"use client";

import { useEffect, useState } from "react";

export default function Home() {
  const [tables, setTables] = useState([]);

  useEffect(() => {
    // main.py의 /table 엔드포인트로 GET 요청을 보냅니다.
    fetch("http://localhost:8000/table")
      .then((response) => response.json())
      .then((data) => {
        console.log(data.tables);
        // 서버로부터 받은 테이블 정보를 상태에 저장합니다.
        setTables(data.tables);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []); // 컴포넌트가 마운트될 때 한 번만 요청을 보내도록 합니다.
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div>
        <h2>Tables:</h2>
        <ul>
          {tables.map((table, index) => (
            <li key={index}>{table}</li>
          ))}
        </ul>
      </div>
    </main>
  );
}
