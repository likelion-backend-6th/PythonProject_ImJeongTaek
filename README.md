## 1. 미션 요구사항 분석 & 체크리스트

---

### 1-1. 미션 요구사항 분석

---

```
1. CLI 기반 메뉴
    - 사용자는 콘솔을 통해 메뉴를 선택할 수 있습니다.
    - 사용자가 선택한 메뉴에 따라 해당 기능을 실행합니다.
    - 사용자는 메뉴를 통해 프로그램을 종료할 수 있습니다.
    - 사용자는 메뉴를 통해 처음 메뉴로 돌아갈 수 있습니다.
2. 데이터 입력 기능
    - 사용자는 콘솔을 통해 도서의 정보를 입력하여 데이터베이스에 저장합니다.
    - 도서의 정보는 ID, 제목, 저자, 출판사 정보를 포함합니다.
3. 도서 정보 조회 기능
    - 사용자는 도서의 ID 혹은 제목을 입력하여 도서의 정보를 조회 합니다.
    - 도서의 정보는 도서의 ID, 제목, 저자, 출판사 정보를 포함합니다.
    - 도서의 대출상태를 표시합니다.
4. 도서 대출 기능
    - 사용자는 콘솔을 통해 도서의 ID 혹은 제목을 입력하여 도서를 대출합니다.
    - 대출하면 도서의 상태는 대출중으로 바뀝니다.
5. 도서 반납 기능
    - 반납을 원하는 도서의 ID 혹은 제목을 입력하여 반납합니다.
    - 반납하면 도서의 상태가 대출가능으로 바뀝니다.
6. 대출 정보 조회 기능
    - 대출한 도서의 정보를 모두 조회할 수 있습니다.
    - 대출 정보는 도서의 ID, 제목, 저자, 출판사, 대출 날짜로 구성됩니다.            
```

### 1-2. 미션 체크리스트

---
```
1. CLI 기반 메뉴
    - 메뉴 선택 하여 기능 실행 [v]
    - 메뉴 선택 하여 프로그램 종료 [v]
    - 메뉴 선택 하여 처음 메뉴로 돌아가기 [v]
2. 데이터 입력 기능
    - 콘솔 입력을 통해 도서의 정보를 데이터 베이스에 저장 [ ]
3. 도서 정보 조회 기능
    - 사용자가 콘솔 입력을 통해 도서의 정보를 조회 [v]
4. 도서 대출 기능
    - 사용자가 콘솔 입력을 통해 도서 정보를 입력하여 대출하고 대출중으로 바뀜 [v]
5. 도서 반납 기능
    - 사용자가 콘솔 입력을 통해 대출하고 싶은 도서를 입력 [v]
    - 입력한 도서의 정보가 대출 가능으로 바뀜 [v]
6. 대출 정보 조회 기능
    - 대출한 도서의 정보를 조회 [v]         
```

## 2. 미션 진행 & 회고

---

### 2-1. 미션 진행 내용 요약

---

```markdown
일단은 기능을 하게끔 만들려고 직독직해 하는 느낌으로 만들었다.
콘솔 메뉴에서 이전 메뉴로 가게 만드는게 힘들어서 메뉴를 없에고 처음으로 가는 것만 만들었다.
조회나 대출, 반납 같은 기능들은 데이터베이스에서 직접 가져오고 수정했다.
```

### 2-2. 회고

---

```markdown
대출기능이 중복 대출이 가능해져 버려서 아쉬웠다.
제목에 숫자랑 글자랑 같이 있다면 기능에서 에러가 날 거 같다.
반납 기능을 어떻게 이용해야 할지 몰라서 반납 날짜 추가를 안해놨다.
```