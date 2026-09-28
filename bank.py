"""Банковский счёт с запретом отрицательного остатка."""

from __future__ import annotations

from money.policy import accept_deposit, accept_withdrawal


class Account:
    """Хранит целочисленный остаток и меняет его только допустимой операцией."""

    def __init__(self, balance: int = 0) -> None:
        self.balance = balance

    def deposit(self, amount: int) -> int:
        accept_deposit(amount)
        self.balance += amount
        return self.balance

    def withdraw(self, amount: int) -> int:
        # Исключение возникает до изменения поля balance.
        accept_withdrawal(self.balance, amount)
        self.balance -= amount
        return self.balance
