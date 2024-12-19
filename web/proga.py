import pyodbc

# Устанавливаю соединение с вашей базой данных
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=db2;DATABASE=qtcourse;UID=lodin;PWD=password')
cursor = conn.cursor()

# Таблица
cursor.execute('''
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='dictionary' AND xtype='U')
CREATE TABLE dictionary (
    id INT IDENTITY(1,1) PRIMARY KEY,
    word NVARCHAR(100) UNIQUE NOT NULL,
    definition NVARCHAR(255) NOT NULL
)
''')
conn.commit()

# Функции для выполнения разных действий слов из базы данных/словаря
def add_word(word, definition):
    try:
        cursor.execute('INSERT INTO dictionary (word, definition) VALUES (?, ?)', (word, definition))
        conn.commit()
        print(f'Слово "{word}" добавлено.')
    except pyodbc.IntegrityError:
        print(f'Слово "{word}" уже существует.')


def search_word(word):
    cursor.execute('SELECT definition FROM dictionary WHERE word = ?', (word,))
    result = cursor.fetchone()
    if result:
        print(f'Определение для "{word}": {result[0]}')
    else:
        print(f'Слово "{word}" не найдено.')


def delete_word(word):
    cursor.execute('DELETE FROM dictionary WHERE word = ?', (word,))
    conn.commit()
    if cursor.rowcount > 0:
        print(f'Слово "{word}" удалено.')
    else:
        print(f'Слово "{word}" не найдено.')


def main():
    while True:
        print("\nВыберите действие:")
        print("1. Добавить слово")
        print("2. Найти слово")
        print("3. Удалить слово")
        print("4. Выход")

        choice = input("Введите номер действия: ")

        if choice == '1':
            word = input("Введите слово: ")
            definition = input("Введите определение: ")
            add_word(word, definition)
        elif choice == '2':
            word = input("Введите слово для поиска: ")
            search_word(word)
        elif choice == '3':
            word = input("Введите слово для удаления: ")
            delete_word(word)
        elif choice == '4':
            break
        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()

# Закрываем соединение с базой данных
conn.close()
