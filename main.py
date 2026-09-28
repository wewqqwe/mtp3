"""Демонстрация классов лабораторной работы №3."""

from __future__ import annotations

import sqlite3
import tempfile
from pathlib import Path

from animals import Animal, Dog
from bank import Account
from filebox import FileBox
from orders import Cart, Product
from orm import Table


def main() -> None:
    account = Account(180)
    print(f"Остаток после взноса: {account.deposit(40)}")
    print(f"Остаток после снятия: {account.withdraw(25)}")
    print(f"Реплика животного: {Animal().speak()}")
    print(f"Реплика собаки: {Dog().speak()}")

    product = Product("КМП-3", "Компас", 375)
    cart = Cart()
    cart.add(product)
    print(f"В корзине: {cart.contents()[0].sku}")

    with tempfile.TemporaryDirectory() as folder:
        root = Path(folder)
        box = FileBox(root / "note.txt")
        box.write("Полевая запись варианта")
        print(f"Содержимое файла: {box.read()}")

        connection = sqlite3.connect(root / "demo.db")
        try:
            table = Table(connection)
            saved = table.insert({"name": "Чертёж"})
            loaded = table.select(saved["id"])
            print(f"Строка мини-ORM: {loaded}")
        finally:
            connection.close()


if __name__ == "__main__":
    main()
