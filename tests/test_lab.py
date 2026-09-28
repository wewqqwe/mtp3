"""Проверки лабораторной работы №3. Классы поставки, без подмен."""

from __future__ import annotations

import sqlite3
import subprocess
import sys
from pathlib import Path

import pytest

from animals import Animal, Dog
from bank import Account
from filebox import FileBox
from orders import Cart, Product
from orm import Table

ROOT = Path(__file__).resolve().parents[1]


def test_account_deposit_withdraw_and_overdraft() -> None:
    account = Account(0)
    assert account.deposit(80) == 80
    assert account.withdraw(30) == 50
    with pytest.raises(ValueError):
        account.withdraw(51)
    assert account.balance == 50
    with pytest.raises(ValueError):
        account.deposit(-1)
    assert account.balance == 50
    assert account.withdraw(50) == 0
    with pytest.raises(ValueError):
        account.withdraw(1)
    assert account.balance == 0


def test_negative_withdrawal_keeps_balance() -> None:
    account = Account(15)
    with pytest.raises(ValueError):
        account.withdraw(-3)
    assert account.balance == 15


def test_dog_speak_differs_and_barks() -> None:
    animal_line = Animal().speak()
    dog_line = Dog().speak()
    assert dog_line != animal_line
    assert "Гав" in dog_line
    assert "Гав" not in animal_line


def test_file_box_roundtrip(tmp_path: Path) -> None:
    target = tmp_path / "sheet.txt"
    box = FileBox(target)
    box.write("полевая запись")
    assert box.read() == "полевая запись"
    assert target.read_text(encoding="utf-8") == "полевая запись"


def test_cart_returns_added_product() -> None:
    product = Product("АР-3", "Альбом", 410)
    cart = Cart()
    cart.add(product)
    found = cart.contents()
    assert len(found) == 1
    assert found[0] is product
    assert found[0].sku == "АР-3"
    assert found[0].title == "Альбом"
    assert found[0].price == 410


def test_orm_insert_then_select(tmp_path: Path) -> None:
    connection = sqlite3.connect(tmp_path / "registry.db")
    try:
        table = Table(connection)
        stored = table.insert({"name": "Сирень"})
        loaded = table.select(stored["id"])
        assert loaded is not None
        assert loaded["name"] == "Сирень"
        second = table.insert({"name": "Краска", "qty": 2})
        fetched = table.select(second["id"])
        assert fetched is not None
        assert fetched["name"] == "Краска"
        assert fetched["qty"] == 2
        assert table.select(999_999) is None
    finally:
        connection.close()


def test_demo_exits_cleanly() -> None:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "main.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr
