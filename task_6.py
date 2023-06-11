import sqlite3
import csv
from utils import validate_input


def calculate_sum():
    with open('numbers.txt', 'r') as num_file:
        count = sum(map(float, num_file.readlines()))

    with open('sum_numbers.txt', 'w') as sum_file:
        sum_file.write(str(count))


def check_even_or_not(number):
    with open('even_or_not_number.txt', 'w') as result_file:
        x = ' ' if (number % 2) == 0 else 'not'
        result_file.write(f'{number} is{x}even number')


def text_output():
    with open('learning_python.txt', 'r') as text_file:
        lines = [line.strip() for line in text_file.readlines()]
    print(lines)


def replace_text():
    print(open('learning_python.txt', 'r').read().replace('Python', 'C'))


def ask_name():
    while True:
        name = input('What is your name? (If you want to leave - write STOP) ')
        if name == 'STOP':
            break
        welcome = f'Hello, {name} \n'

        with open('guest_book.txt', 'a') as guests_file:
            guests_file.write(welcome)
        print(welcome)


def count_word_the():
    book_list = ['Earle_Wayne.txt', 'History_of_the_US.txt', 'Lilith.txt']
    for book in book_list:
        with open(book, encoding='utf-8') as amount_file:
            blist = amount_file.read()
            count = blist.lower().count('the')
            print(f'In {book} word the appears {count} times')


def replace_gaps():
    ftext = open('History_Zionism.txt', 'r', encoding='utf-8').read().replace('\n', ' ')
    with open('formatted_text.txt', 'w', encoding='utf-8') as format_text:
        format_text.write(ftext)


def find_header():
    with open('Robin.txt', 'r', encoding='utf-8') as book:
        robin = book.read()

    with open('chapters.txt', 'w', encoding='utf-8') as header_file:
        header_file.writelines(head for head in robin.split('\n') if head.startswith('CHAPTER'))


def find_percent():
    count_low = 0
    count_up = 0
    with open('Monte_Cristo.txt', 'r', encoding='utf-8') as book:
        cristo = book.read()
    count_all = len(cristo)
    for cr in cristo:
        if cr.islower():
            count_low += 1
        elif cr.isupper():
            count_up += 1

    low = (count_low / count_all) * 100
    up = (count_up / count_all) * 100

    print(f'Percent of small letters in text is {low}%')
    print(f'Percent of capital letters in text is {up}%')


def work_with_database():
    conn = sqlite3.connect('imdb.db')
    curs = conn.cursor()
    curs.execute('''CREATE TABLE ratings (id INTEGER PRIMARY KEY, title
    VARCHAR(20), year INT, rating FLOAT)''')

    with open('imdb.csv', 'r') as db_file:
        readcsv = csv.reader(db_file)
    for line in readcsv:
        curs.execute('INSERT INTO ratings (title, year, rating) VALUES(?, ?, ?)',
                     (line[0], line[1], line[2], line[3]))

    curs.execute('SELECT * FROM ratings ORDER BY title')
    rows = curs.fetchall()
    print(rows)

    curs.execute('SELECT * FROM ratings WHERE rating > 8.70)')
    rows = curs.fetchall()
    print(rows)

    curs.close()
    conn.close()


if __name__ == '__main__':
    calculate_sum()

    num = validate_input('even number ', int)
    check_even_or_not(num)

    text_output()
    replace_text()
    ask_name()
    count_word_the()
    replace_gaps()
    find_header()
    find_percent()
    work_with_database()
