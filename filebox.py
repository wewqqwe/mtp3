"""Класс доступа к одному текстовому файлу на диске."""

from __future__ import annotations

from pathlib import Path

from cabinet.texts import read_text, write_text


class FileBox:
    """Читает и записывает файл по пути, переданному в конструктор."""

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    def write(self, text: str) -> None:
        write_text(self.path, text)

    def read(self) -> str:
        return read_text(self.path)
