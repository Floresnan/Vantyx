import sqlite3
from datetime import datetime


class MemoryService:

    def __init__(self, db_path="vantyx.db"):
        self.db_path = db_path
        self._create_tables()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _create_tables(self):

        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS lead_memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lead_nome TEXT,
            evento TEXT,
            detalhe TEXT,
            data TEXT
        )
        """)

        conn.commit()
        conn.close()

    def registrar_evento(self, lead_nome, evento, detalhe=""):

        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO lead_memory (lead_nome, evento, detalhe, data)
        VALUES (?, ?, ?, ?)
        """, (lead_nome, evento, detalhe, datetime.now().isoformat()))

        conn.commit()
        conn.close()

    def buscar_memoria(self, lead_nome):

        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT evento, detalhe, data
        FROM lead_memory
        WHERE lead_nome = ?
        ORDER BY data DESC
        """, (lead_nome,))

        resultados = cursor.fetchall()

        conn.close()

        return resultados
