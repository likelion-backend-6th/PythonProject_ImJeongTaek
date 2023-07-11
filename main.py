import psycopg2


# # 데이터베이스에 데이터 추가
# conn = psycopg2.connect(
#     host='localhost',
#     dbname='library2',
#     user='user2',
#     password='1234',
# )
#
# cur = conn.cursor()
#
#
#
# cur.execute("INSERT INTO Books(book_id, title, author, publisher, loan_available) "
#             "VALUES (002, '파이썬으로 배우는 알고리즘', '이영희', '정보과학사', TRUE),"
#             "(003, '빅데이 분석을 위한 파이썬', '최민수', '한빛미디어', TRUE),"
#             "(004, '머신러닝 입문 with 파이썬', '박영미', '청람출판사', TRUE),"
#             "(005, '파이썬과 함께하는 딥러닝 이야기', '조재호', '비제이퍼블릭', TRUE)")
# conn.commit()
#
# cur.close()
# conn.close()


# 터미널에서 생성
# cur.execute('''
# CREATE TABLE Books (
# book_id PRIMARY KEY,
# title VARCHAR(100),
# author VARCHAR(50),
# publisher VARCHAR(50),
# is_available BOOLEAN DEFAULT TRUE))
# ''')

# cur.execute('''
# CREATE TABLE Loans (
# loan_id SERIAL PRIMARY KEY,
# loaned_book_id INTEGER REFERENCES Books(book_id),
# Loan_date DATE NOT NULL,
# Return_date DATE NULL)
# ''')


def library_menu():
    print('\n-----------------------------------')
    print('도서관 관리 시스템 메인 메뉴'.center(30))
    print('-----------------------------------')
    print('1. 도서 정보 조회')
    print('2. 도서 등록')
    print('3. 도서 대출')
    print('4. 도서 반납')
    print('5. 대출 정보 조회')
    print('6. 종료')


def sub_menu():
    print('-----------------------------------')
    print('1. 처음으로 돌아가기')
    print('2. 종료')
    sub_choice = input('\n원하시는 번호를 선택해 주세요. :')
    if sub_choice == '1':
        library_menu()
    elif sub_choice == '2':
        print('\n수고하셨습니다.')
        exit()
    else:
        print('다시 입력해주세요.')
        sub_menu()


def book_info(data):
    conn = psycopg2.connect(
        host='localhost',
        dbname='library2',
        user='user2',
        password='1234',
    )

    cur = conn.cursor()
    if data.isnumeric():
        cur.execute(f"SELECT * FROM Books WHERE book_id = {data}")
        selected = cur.fetchall()
        if len(selected) == 0:
            print('\n없는 ID입니다. 다시 선택해주세요')
            sub_menu()
        else:
            print('\nID        TITLE         AUTHOR   PUBLISHER   LOAN_AVAILABLE')
            for row in selected:
                print(row)
            sub_menu()
    elif data:
        cur.execute(f"SELECT * FROM Books WHERE title LIKE '%{data}%'")
        selected = cur.fetchall()
        print('\nID        TITLE         AUTHOR   PUBLISHER   LOAN_AVAILABLE')
        for row in selected:
            print(row)
        sub_menu()
    cur.close()
    conn.close()


def book_registration():
    conn = psycopg2.connect(
        host='localhost',
        dbname='library2',
        user='user2',
        password='1234',
    )
    cur = conn.cursor()

    print('-----------------------------------')
    book_id = input('도서의 ID를 입력해주세요. :')
    title = input('도서의 제목을 입력해주세요. :')
    author = input('도서의 저자를 입력해주세요. :')
    publisher = input('도서의 출판사를 입력해주세요. :')

    cur.execute(f"INSERT INTO Books (book_id, title, author, publisher) VALUES ({book_id}, '{title}', '{author}', '{publisher}')")
    conn.commit()

    print('\n도서 등록을 완료하였습니다.')
    sub_menu()
    cur.close()
    conn.close()


def loan_book():
    conn = psycopg2.connect(
        host='localhost',
        dbname='library2',
        user='user2',
        password='1234',
    )

    cur = conn.cursor()

    cur.execute("SELECT * FROM Books WHERE loan_available = TRUE ORDER BY book_id")
    selected = cur.fetchmany(5)
    print('-----------------------------------')
    print('\nID        TITLE         AUTHOR   PUBLISHER   LOAN_AVAILABLE')
    for row in selected:
        print(row)
    data = input('\n대출하고 싶은 책의 ID 또는 제목을 입력하세요. :')
    if data.isnumeric():
        cur.execute(f"SELECT book_id FROM Books")
        book_id = cur.fetchall()
        if (int(data),) in book_id:
            cur.execute(f"UPDATE Books SET loan_available = FALSE WHERE book_id={data}")
            cur.execute(f"INSERT INTO Loans (loaned_book_id, loan_date) VALUES ({data}, current_date)")
            conn.commit()
            print('\n대출해주셔서 감사합니다.')
            sub_menu()
        else:
            print('\n없는 ID입니다. 다시 선택해주세요')
            sub_menu()

    else:
        cur.execute(f"SELECT title FROM Books")
        title = cur.fetchall()
        if (data,) in title:
            cur.execute(f"UPDATE Books SET loan_available = FALSE WHERE title = '{data}'")
            cur.execute(f"SELECT book_id FROM Books WHERE loan_available = FALSE")
            selected = cur.fetchone()
            cur.execute(f"INSERT INTO Loans (loaned_book_id, loan_date) VALUES ({selected[0]}, current_date)")
            conn.commit()
            print('\n대출해주셔서 감사합니다.')
            sub_menu()
        else:
            print('\n없는 ID입니다. 다시 선택해주세요')
            sub_menu()

    cur.close()
    conn.close()


def return_book():
    conn = psycopg2.connect(
        host='localhost',
        dbname='library2',
        user='user2',
        password='1234',
    )

    cur = conn.cursor()
    cur.execute("SELECT book_id, title, author, publisher FROM Books WHERE loan_available = FALSE ORDER BY book_id")
    selected = cur.fetchmany(5)
    print('-----------------------------------')
    print('\nID        TITLE         AUTHOR   PUBLISHER')
    for row in selected:
        print(row)
    data = input('\n반납하고 싶은 책의 ID 또는 제목을 입력하세요. :')
    if data.isnumeric():
        cur.execute(f"SELECT book_id FROM Books")
        book_id = cur.fetchall()
        if (int(data),) in book_id:
            cur.execute(f"UPDATE Books SET loan_available = TRUE WHERE book_id={data}")
            cur.execute(f"DELETE FROM Loans WHERE loaned_book_id = {data}")
            conn.commit()
            print('\n반납해주셔서 감사합니다.')
            sub_menu()
        else:
            print('\n없는 ID입니다. 다시 선택해주세요')
            sub_menu()

    else:
        cur.execute(f"SELECT title FROM Books")
        title = cur.fetchall()
        if (data,) in title:
            cur.execute(f"UPDATE Books SET loan_available = TRUE WHERE title = '{data}'")
            cur.execute(f"SELECT book_id FROM Books WHERE title = '{data}'")
            selected = cur.fetchone()
            cur.execute(f"DELETE FROM Loans WHERE loaned_book_id = {selected[0]}")
            conn.commit()
            print('\n대출해주셔서 감사합니다.')
            sub_menu()
        else:
            print('\n없는 ID입니다. 다시 선택해주세요')
            sub_menu()

    cur.close()
    conn.close()


def is_loaned():
    conn = psycopg2.connect(
        host='localhost',
        dbname='library2',
        user='user2',
        password='1234',
    )

    cur = conn.cursor()
    print('-----------------------------------')
    cur.execute(
        "SELECT book_id, title, author, publisher, TO_CHAR(loan_date, 'YYYYMMDD') AS loan_date_number FROM Books JOIN Loans ON Books.book_id = Loans.loaned_book_id")
    rows = cur.fetchall()

    for row in rows:
        book_id, title, author, publisher, loan_date_number = row
        print(
            f"Book ID: {book_id}, Title: {title}, Author: {author}, Publisher: {publisher}, Loan Date: {loan_date_number}")

    sub_menu()
    cur.close()
    conn.close()


library_menu()
while True:
    print()
    choice = int(input('원하시는 번호를 입력해 주세요. : '))

    if choice == 1:
        print('-----------------------------------')
        info = input('도서의 ID 혹은 제목을 입력해주세요. : ')
        book_info(info)
    elif choice == 2:
        book_registration()
    elif choice == 3:
        loan_book()
    elif choice == 4:
        return_book()
    elif choice == 5:
        is_loaned()
    elif choice == 6:
        print('\n수고하셨습니다.')
        break
    else:
        print('\n다시 입력해 주세요.')
        library_menu()
