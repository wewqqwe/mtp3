"""Иерархия Животное→Собака с различной речью."""

from __future__ import annotations

from voices.phrases import DOG_BARK, QUIET_ANIMAL


class Animal:
    """Базовое животное. Реплика не совпадает с репликой собаки."""

    def speak(self) -> str:
        return QUIET_ANIMAL


class Dog(Animal):
    """Собака переопределяет речь и отвечает лаем."""

    def speak(self) -> str:
        return DOG_BARK
