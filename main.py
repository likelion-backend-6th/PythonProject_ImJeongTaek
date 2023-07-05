import psycopg2

conn = psycopg2.connect(
    host='localhost',
    dbname='library2',
    user='user2',
    password='1234',
)

cur = conn.cursor()

cur.close()
conn.close()


def library_menu():
    print('\n-----------------------------------')
    print('도서관 관리 시스템 메인 메뉴'.center(30))
    print('-----------------------------------')
    print('1. 도서 정보 조회')
    print('2. 도서 대출')
    print('3. 도서 반납')
    print('4. 대출 정보 조회')
    print('5. 종료')


while True:
    library_menu()
    print()
    choice = int(input('원하시는 번호를 입력해 주세요.: '))

    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        print('\n수고하셨습니다.')
        break
    else:
        print('\n다시 입력해 주세요.')
