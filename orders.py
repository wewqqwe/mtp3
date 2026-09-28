"""Товар и корзина заказа."""

from __future__ import annotations


class Product:
    """Позиция каталога: артикул, название и цена в целых единицах."""

    def __init__(self, sku: str, title: str, price: int) -> None:
        self.sku = sku
        self.title = title
        self.price = price

    def __repr__(self) -> str:
        return (
            f"Product(sku={self.sku!r}, title={self.title!r}, "
            f"price={self.price!r})"
        )


class Cart:
    """Корзина сохраняет товары в порядке добавления."""

    def __init__(self) -> None:
        self._goods: list[Product] = []

    def add(self, product: Product) -> None:
        self._goods.append(product)

    def contents(self) -> list[Product]:
        # Копия списка защищает внутреннее хранилище, объекты товаров те же.
        return list(self._goods)
