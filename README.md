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
