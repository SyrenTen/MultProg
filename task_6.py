import sqlite3
import csv
from utils import validation


def task_6_p1():
    with open('numbers.txt', 'r') as task6p1:
        count = sum(map(float, task6p1.readlines()))

    with open('sum_numbers.txt', 'w') as task6p1:
        task6p1.write(str(count))


def task_6_p2(even_number):
    with open('even_number.txt', 'w') as task6p2:
        if (even_number % 2) == 0:
            task6p2.write(f'{even_number} is even number')
        else:
            task6p2.write(f'{even_number} is not even number')


def task_6_p3():
    lines = []
    with open('learning_python.txt', 'r') as task6p3:
        line = task6p3.readline()
        while line:
            lines.append(line.strip())
            line = task6p3.readline()

    print(lines)


def task_6_p4():
    with open('learning_python.txt', 'r') as task6p4:
        new_list = task6p4.read()
    func_repl = new_list.replace('Python', 'C')
    print(func_repl)


def task_6_p5():
    open('guest_book.txt', 'w')
    while True:
        name = input('What is your name? (If you want to leave - write STOP) ')
        if name == 'STOP':
            exit()
        welcome = f'Hello, {name} \n'

        with open('guest_book.txt', 'a') as task6p5:
            task6p5.write(welcome)
        print(welcome)


def task_6_p6():
    book_list = ['Earle_Wayne.txt', 'History_of_the_US.txt', 'Lilith.txt']
    for books in book_list:
        with open(books, encoding='utf-8') as task6p6:
            blist = task6p6.read()
            count = blist.lower().count('the')
            print(f'In {books} word the appears {count} times')


def task_6_p7():
    with open('History_Zionism.txt', 'r', encoding='utf-8') as newtext:
        copytext = newtext.read()
        ftext = copytext.replace('\n', ' ')
    with open('formatted_text.txt', 'w', encoding='utf-8') as task6p7:
        task6p7.write(ftext)


def task_6_p8():
    with open('Robin.txt', 'r', encoding='utf-8') as task6p6:
        robin = task6p6.read()

    with open('chapters.txt', 'w', encoding='utf-8') as task66:
        task66.writelines(head for head in robin.split('\n') if head.startswith('CHAPTER'))


def task_6_p9():
    countlow = 0
    countup = 0
    with open('Monte_Cristo.txt', 'r', encoding='utf-8') as part9:
        cristo = part9.read()
    countall = len(cristo)
    for cr in cristo:
        if cr.isalpha() and cr.islower():
            countlow += 1
        if cr.isalpha() and cr.isupper():
            countup += 1

    low = (countlow / countall) * 100
    up = (countup / countall) * 100

    print(f'Percent of small letters in text is {low}%')
    print(f'Percent of capital letters in text is {up}%')


def task_6_p10():
    conn = sqlite3.connect('imdb.db')
    curs = conn.cursor()
    curs.execute('''CREATE TABLE ratings (id INTEGER PRIMARY KEY, title
    VARCHAR(20), year INT, rating FLOAT)''')

    with open('imdb.csv', 'r') as task6p10:
        readcsv = csv.reader(task6p10)
    for line in readcsv:
        curs.execute('INSERT INTO ratings (title, year, rating) VALUES(?, ?, ?)',
                     (line[0], line[1], line[2], line[3]))
        # I'm not sure if it's right :/

    curs.execute('SELECT * FROM ratings ORDER BY title')
    rows = curs.fetchall()
    print(rows)

    curs.execute('SELECT * FROM ratings WHERE rating > 8.70)')
    rows = curs.fetchall()
    print(rows)

    curs.close()
    conn.close()


if __name__ == '__main__':
    task_6_p1()

    num = validation('even number ', int)
    task_6_p2(num)

    task_6_p3()
    task_6_p4()
    task_6_p5()
    task_6_p6()
    task_6_p7()
    task_6_p8()
    task_6_p9()
    task_6_p10()
