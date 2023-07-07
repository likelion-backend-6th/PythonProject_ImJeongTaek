import psycopg2
import re


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
# loan_id PRIMARY KEY,
# loaned_book_id INTEGER REFERENCES Books(book_id),
# Loan_date DATE NOT NULL,
# Return_date DATE NULL))
# ''')


def library_menu():
    print('\n-----------------------------------')
    print('도서관 관리 시스템 메인 메뉴'.center(30))
    print('-----------------------------------')
    print('1. 도서 정보 조회')
    print('2. 도서 대출')
    print('3. 도서 반납')
    print('4. 대출 정보 조회')
    print('5. 종료')


def sub_menu():
    print('-----------------------------------')
    print('1. 처음으로 돌아가기')
    print('2. 종료')
    sub_choice = input('\n원하시는 번호를 선택해 주세요. :')
    if sub_choice == '1':
        library_menu()
    elif sub_choice == '2':
        print('\n수고하셨습니다.')
        conn.close()
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
        # num_data = re.sub(r'\D', '', data)
        cur.execute(f"SELECT * FROM Books WHERE book_id = {data}")
        selected = cur.fetchall()
        print('\nID        TITLE         AUTHOR   PUBLISHER   LOAN_AVAILABLE')
        print(selected)
    elif data:
        cur.execute(f"SELECT * FROM Books WHERE title LIKE '%{data}%'")
    selected = cur.fetchall()
    print('\nID        TITLE         AUTHOR   PUBLISHER   LOAN_AVAILABLE')
    print(selected)

    sub_menu()
    cur.close()
    conn.close()


def loan_book():
    pass

def return_book():
    pass


def is_loaned():
    pass


library_menu()
while True:
    print()
    choice = int(input('원하시는 번호를 입력해 주세요. : '))

    if choice == 1:
        print('-----------------------------------')
        info = input(('도서의 ID 혹은 제목을 입력해주세요. : '))
        book_info(info)
    elif choice == 2:
        loan_book()
    elif choice == 3:
        return_book()
    elif choice == 4:
        is_loaned()
    elif choice == 5:
        print('\n수고하셨습니다.')
        break
    else:
        print('\n다시 입력해 주세요.')
        library_menu()
