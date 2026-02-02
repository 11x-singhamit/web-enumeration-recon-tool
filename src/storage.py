import sqlite3
from datetime import datetime


class ResultStorage:
    def __init__(self):
        self.db_path = "data/results.db"
        self.txt_path = "data/results.txt"

        self.conn = sqlite3.connect(self.db_path)
        self.create_table()

    def create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT,
            scanned_at TEXT
        )
        """)
        self.conn.commit()

    def save(self, urls):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save to database
        for url in urls:
            self.conn.execute(
                "INSERT INTO results (url, scanned_at) VALUES (?, ?)",
                (url, timestamp)
            )
        self.conn.commit()

        # Save to text file
        with open(self.txt_path, "a") as file:
            file.write(f"\nScan Time: {timestamp}\n")
            for url in urls:
                file.write(url + "\n")
