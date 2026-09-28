"""Строка таблицы: полезная нагрузка хранится целиком как JSON."""

from __future__ import annotations

import json
import sqlite3

_SCHEMA = """
CREATE TABLE IF NOT EXISTS sheet (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    body TEXT NOT NULL
)
"""


def prepare(connection: sqlite3.Connection) -> None:
    connection.execute(_SCHEMA)
    connection.commit()


def insert_body(connection: sqlite3.Connection, payload: dict) -> dict:
    encoded = json.dumps(payload, ensure_ascii=False)
    cursor = connection.execute(
        "INSERT INTO sheet (body) VALUES (?)",
        (encoded,),
    )
    connection.commit()
    identifier = cursor.lastrowid
    if not isinstance(identifier, int):
        raise RuntimeError("База не вернула идентификатор вставленной строки.")
    stored = dict(payload)
    stored["id"] = identifier
    return stored


def fetch_body(connection: sqlite3.Connection, row_id: int) -> dict | None:
    row = connection.execute(
        "SELECT id, body FROM sheet WHERE id = ?",
        (row_id,),
    ).fetchone()
    if row is None:
        return None
    loaded = json.loads(row[1])
    if not isinstance(loaded, dict):
        raise ValueError("В строке таблицы ожидался JSON-объект.")
    restored = dict(loaded)
    restored["id"] = row[0]
    return restored
