import sqlite3
from pathlib import Path
from threading import Lock

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Database folder
DB_DIR = BASE_DIR / "database"
DB_DIR.mkdir(exist_ok=True)

# Database file
DB_PATH = DB_DIR / "friday.db"


class Database:

    def __init__(self):
        self.lock = Lock()

        self.connection = sqlite3.connect(
            DB_PATH,
            check_same_thread=False
        )

        self.connection.row_factory = sqlite3.Row

        self.create_tables()

    def create_tables(self):

        with self.lock:
            cursor = self.connection.cursor()

            # ==========================
            # Memories
            # ==========================
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS memories (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                category TEXT NOT NULL,

                key TEXT NOT NULL,

                value TEXT NOT NULL,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)

            # ==========================
            # Conversations
            # ==========================
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS conversations (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                role TEXT NOT NULL,

                message TEXT NOT NULL,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)

            self.connection.commit()

    def execute(self, query, params=()):

        with self.lock:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            return cursor

    def fetchall(self, query, params=()):

        with self.lock:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()

    def fetchone(self, query, params=()):

        with self.lock:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            return cursor.fetchone()

    def close(self):
        with self.lock:
            self.connection.close()


db = Database()