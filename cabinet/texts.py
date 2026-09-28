"""Запись и чтение одного текстового файла."""

from __future__ import annotations

from pathlib import Path


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")
