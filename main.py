import sqlite3

conn = sqlite3.connect('notes.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS notes
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT,
                   content TEXT)''')

def create_note():
    title = input("Введите заголовок записи: ")
    content = input("Введите содержимое записи: ")
    cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    print("Запись успешно создана!")


def edit_note():
    note_id = input("Введите ID записи, которую хотите редактировать: ")
    title = input("Введите новый заголовок записи: ")
    content = input("Введите новое содержимое записи: ")
    cursor.execute("UPDATE notes SET title=?, content=? WHERE id=?", (title, content, note_id))
    conn.commit()
    print("Запись успешно отредактирована!")


def delete_note():
    note_id = input("Введите ID записи, которую хотите удалить: ")
    cursor.execute("DELETE FROM notes WHERE id=?", (note_id,))
    conn.commit()
    print("Запись успешно удалена!")


def display_notes():
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    for note in notes:
        print(f"ID: {note[0]}, Заголовок: {note[1]}, Содержимое: {note[2]}")


while True:
    print("1. Создать новую запись")
    print("2. Редактировать существующую запись")
    print("3. Удалить существующую запись")
    print("4. Вывести все записи")
    print("5. Выйти из приложения")
    choice = input("Выберите действие: ")

    if choice == "1":
        create_note()
    elif choice == "2":
        edit_note()
    elif choice == "3":
        delete_note()
    elif choice == "4":
        display_notes()
    elif choice == "5":
        break
    else:
        print("Некорректный ввод. Пожалуйста, выберите действие из списка.")


conn.close()
