const fs = require("fs");
const { DateTime } = require("luxon");
// npn install luxon으로 설치하면 된다.

function nowTime() {
  const time = DateTime.now().toFormat("yyyy-MM-dd-HH-mm-ss");
  return time;
}

function generateYoonValues(name, index) {
  for (let i = 1; i < index; i++) {
    // 현재시간
    const now = nowTime();
    const directoryName = `${now} ${name}-${i}`;

    // 디렉토리 생성
    fs.mkdirSync(directoryName);
    const directoryPath = directoryName;

    if (fs.existsSync(directoryPath)) {
      console.log("디렉토리가 존재합니다.");
      const fileName = `${directoryName}/${name}-${i}.txt`;
      fs.writeFileSync(fileName, "This is a sample text.");
    } else {
      console.log("디렉토리가 존재하지 않습니다.");
      continue;
    }
  }
}

generateYoonValues("yoon", 3);
