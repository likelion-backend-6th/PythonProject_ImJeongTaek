<<<<<<< HEAD
# PythonProject_ImJeongTaek

# 프로젝트 개요

## 프로젝트 이름

---

도서관 관리 콘솔 애플리케이션

## 프로젝트 개요

---

본 프로젝트는 Python을 활용하여 콘솔 기반의 도서관 관리 시스템을 개발하는 것을 목표로 합니다. 이 시스템은 도서 대출, 반납, 그리고 회원 관리 기능을 제공합니다.

## 기능 설명

---

### 0. CLI 기반 메뉴 (기본)

- (기본) 사용자는 콘솔을 통해 메뉴를 선택할 수 있습니다.
- (기본) 사용자가 선택한 메뉴에 따라 해당 기능을 실행합니다.
- (기본) 사용자는 메뉴를 통해 프로그램을 종료할 수 있습니다.
- (심화) 사용자는 메뉴를 통해 이전 메뉴로 돌아갈 수 있습니다.
- (심화) 메뉴 선택시 콘솔을 삭제하여 사용자가 선택한 메뉴만 출력합니다.

### 1. 데이터 입력 기능 (기본)

- (기본) 사용자는 콘솔을 통해 도서의 정보를 입력하여 데이터베이스에 저장합니다.
- (기본) 도서의 정보는 도서의 ID, 이름, 저자, 출판사 정보를 포함합니다.
- (심화) 파일을 통해 도서의 정보를 입력하여 데이터베이스에 저장합니다. (csv, json, xml 등)

### 2. 도서 정보 조회 기능 (기본)

- (기본) 사용자는 도서의 ID 혹은 이름을 입력하여 도서의 정보를 조회 합니다.
- (기본) 도서의 정보는 도서의 ID, 이름, 저자, 출판사 정보를 포함합니다.
- (심화) 도서의 상태(대출 가능, 대출 중)가 표시됩니다.
- (심화) 도서의 상태는 도서가 대출 가능한 상태인지, 대출 중인 상태인지를 나타냅니다.
- (심화) 도서가 대출 중인 상태인 경우, 도서의 대출 정보를 함께 출력합니다.

### 3. 도서 대출 기능 (기본)

- (기본) 사용자는 콘솔을 통해 도서의 ID 혹은 이름을 입력하여 도서를 대출합니다.
- (기본) 대출하면 도서의 상태를 대출중으로 변경합니다.
- (심화) 대출중인 도서를 모두 출력합니다.
- (심화) 도서가 이미 대출 중일 경우, 대출이 불가능하다고 출력합니다.

### 4. 도서 반납 기능 (기본)

- (기본) 반납을 원하는 도서의 ID 혹은 이름을 입력하여 반납합니다.
- (기본) 반납하면 도서의 상태가 대출 가능으로 변경됩니다.

### 5. 대출 정보 조회 기능 (심화)

- 대출한 도서의 정보를 모두 조회할 수 있습니다.
- 대출 정보는 도서의 ID, 이름, 저자, 출판사, 대출 날짜, 반납일자로 구성됩니다.
- 대출 정보는 대출 날짜를 기준으로 내림차순으로 정렬됩니다.

### 6. 종료 기능 (기본)

- 사용자는 프로그램을 종료할 수 있습니다.

## 실행환경

---

- Python 3.9 이상
- PostgreSQL 13 이상: 데이터베이스로 사용됩니다.
- psycopg2: Python에서 PostgreSql을 사용하기 위한 패키지입니다.
- PyCharm: Python 개발 환경입니다.
=======
## 1. 미션 요구사항 분석 & 체크리스트

---

### 1-1. 미션 요구사항 분석

---

```
[작성 가이드] 

이 블럭에 있는 내용은 확인 후 지워주세요. 

미션을 확인한 뒤 각 요구사항이 어떤 기능을 하여야 하는지 분석한 내용을 적습니다. 

(작성 TIP) 
이 단락은 어떤 기능을 어떻게 개발을 진행할지에 대한 방향성을 설정하는 단락입니다. 
따라서 스스로 작성해보는 기능 명세라고 생각해주세요. 
```

### 1-2. 미션 체크리스트

---

```
[작성 가이드] 

이 블럭에 있는 내용은 확인 후 지워주세요. 

분석한 내용을 기반으로 어떤 기능을 구현해야 할지에 대해서 체크리스트를 만듭니다. 

(작성 TIP) 
체크리스트 예시는 아래와 같습니다. (개발 진행할 프로세스를 구간별로 나누어보세요.)

[] GitHub 개발과 최종 배포용 브랜치 분리 
[] 상품 조회/수정 API 구현
[] 상품 수정 테스트 코드 작성 
[] 인증/인가 필터 구현
```

## 2. 미션 진행 & 회고

---

### 2-1. 미션 진행 내용 요약

---

```markdown
[작성 가이드] 
이 블럭에 있는 내용은 확인 후 지워주세요. 

*체크리스트를 중심으로 각각의 기능을 구현하기 위해 어떤 생각을 했는지 정리합니다.*

(작성 TIP) 
무엇에 중점을 두고 구현하였는지, 어떤 공식문서나 예제를 참고하여 개발하였는지 뿐만 아니라 
미션을 진행하기 전 개인적으로 실습한 것도 포함하여 작성해주시기 바랍니다.
실제 개발 과정에서 목표하던 바가 무엇이었는지 작성해주시기 바랍니다.
구현 과정에 따라 어떤 결과물이 나오게 되었는지 최대한 상세하게 작성해주시기 바랍니다.
```

### 2-2. 회고

---

```markdown
[작성 가이드] 
이 블럭에 있는 내용은 확인 후 지워주세요. 

*구현 과정에서 아쉬웠던 점 / 궁금했던 점을 정리합니다.*

(작성 TIP) 
추후 리팩토링 시, 어떤 부분을 추가적으로 진행하고 싶은지에 대해 구체적으로 작성해보시기 바랍니다. 
```
>>>>>>> 5a1ea76 (README.md 추가)
