// 요소 선택 변수 지정
let elText = document.getElementById("text_space");
let elChapter = document.getElementById("chapter_space");

// 비동기 데이터 보여주는 함수
async function displayData(book, chapter = 0) {
  // 데이터 추가할 DOM 요소 설정
  const testSpace = document.querySelector("#testSpace");
  // 데이터 가져오기
  let data = await getData(book, chapter);
  testSpace.innerHTML = ""; // 초기화
  for (const obj of data) {
    generateVerse(obj, testSpace); // 구절 데이터 생성
  }
}

// Data 가져오는 fetch
function getData(book, chapter = 0) {
  let url = `/bible/bible/` + encodeURIComponent(book) + "/" + chapter;
  return fetch(url)
    .then((response) => response.json())
    .then((data) => {
      return data;
    })
    .catch((error) => console.error(error));
}

// 장을 표시하는 함수
function displayChapter(book, chapter_length) {
  elChapter.innerHTML = "";
  for (let index = 1; index < chapter_length + 1; index++) {
    span = document.createElement("span");
    span.classList.add("btn", "btn-outline-primary", "btn-sm");
    span.append(`${index}`);
    elChapter.appendChild(span);
    span.addEventListener("click", () => {
      displayData(book, index);
    });
  }
}

function generateVerse(obj, space) {
  // 1절인 경우 장 생성
  if (obj.verse === 1) {
    const div = document.createElement("div");
    div.classList.add("chapter");
    div.textContent = obj.chapter;
    space.append(div);
  }
  // 박스 생성
  const box = document.createElement("div");
  box.classList.add("box");

  // 절 번호 추가
  const verseNumber = document.createElement("div");
  verseNumber.classList.add("verse_number");
  verseNumber.textContent = obj.verse;

  // 절 내용 추가
  const verse = document.createElement("p");
  verse.textContent = obj.contents;

  // 박스에 자식 요소들을 추가
  box.appendChild(verseNumber);
  box.appendChild(verse);

  space.appendChild(box); // HTML 요소에 추가
}

// 타이틀 번경
function setNavTitle(title) {
  document.getElementById("nav-title").innerText = title;
}


/* Dark Mode */
const darkModeIcon = document.getElementById('darkModeIcon');

// 페이지 로드 시 저장된 사용자 환경 설정을 확인하고 반영
if (localStorage.getItem('darkMode') === 'enabled') {
  document.body.classList.add('dark-mode');
}

// 아이콘 클릭 시 다크 모드 설정 변경
darkModeIcon.addEventListener('click', () => {
  document.body.classList.toggle('dark-mode');

  // 다크 모드 상태를 로컬 스토리지에 저장
  if (document.body.classList.contains('dark-mode')) {
    localStorage.setItem('darkMode', 'enabled');
  } else {
    localStorage.setItem('darkMode', 'disabled');
  }
});