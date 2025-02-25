import sqlite3

SCHEMA_PATH="../database/schema.sql"
DB_PATH="../database/tasks.db"
TABLE_NAME='tasks'
# Funkcja do połączenia z bazą danych
def connect_db():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        print("✅ Połączono z bazą danych SQLite")
        return conn, cursor
    except sqlite3.Error as e:
        print(f"❌ Błąd połączenia z bazą: {e}")
        return None, None

# Funkcja do tworzenia tabeli
def create_table():
    conn, cursor = connect_db()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tasks';")
    if cursor.fetchone():
        print("✅ Baza i tabela 'tasks' istnieją!")
    else:
        cursor.execute('''
            CREATE TABLE tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT DEFAULT 'Do zrobienia',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        print("✅️ Tabela została właśnie utworzona.")

    conn.commit()
    conn.close()

def add_task(title,description):
    conn, cursor = connect_db()
    query = f"INSERT INTO {TABLE_NAME} (title, description) VALUES (?, ?)"
    cursor.execute(query,(title,description))

    conn.commit()
    conn.close()
    print(f'Zadanie {title} dodano do bazy')

def show_all_tasks():
    conn, cursor=connect_db()
    query=f"SELECT * FROM {TABLE_NAME}"
    cursor.execute(query)
    results=cursor.fetchall()
    conn.close()
    print('Wyświetlono wszystkie zadania:')
    for row in results:
        print(row)  # Wyświetla każdy rekord w osobnej linii

def delete_task(id):
    conn,cursor=connect_db()
    query=f"DELETE FROM {TABLE_NAME} WHERE id=?"
    cursor.execute(query,(id,))
    conn.commit()
    conn.close()
    print(f'Usunieto zadanie o id={id}')

def update_task(id, newTitle,newDescription,newStatus):
    conn, cursor=connect_db()
    query=f"UPDATE {TABLE_NAME} SET title=?, description=?, status=? WHERE id=?"
    cursor.execute(query,(newTitle,newDescription,newStatus,id))

    conn.commit()
    conn.close()
    print(f'Zaktualizowano zadanie o id={id}')


# Test
if __name__ == "__main__":
    create_table()

update_task(4,'pyt','fajny','Do zrobienia')

show_all_tasks()