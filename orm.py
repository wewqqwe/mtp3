"""Мини-ORM: вставка словаря и выборка строки по идентификатору."""

from __future__ import annotations

import sqlite3

from records.sheet import fetch_body, insert_body, prepare


class Table:
    """Таблица поверх уже открытого соединения sqlite3."""

    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection = connection
        prepare(connection)

    def insert(self, payload: dict) -> dict:
        return insert_body(self.connection, payload)

    def select(self, row_id: int) -> dict | None:
        return fetch_body(self.connection, row_id)
