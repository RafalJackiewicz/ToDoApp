CREATE TABLE tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT DEFAULT 'Do zrobienia',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            