from abc import ABC, abstractmethod


class SortStrategy(ABC):
    """Абстрактный класс для стратегий сортировки"""

    @abstractmethod
    def perform_sort(self, data):
        """
        Абстрактный метод для сортировки
        :param data: список для сортировки
        :return: отсортированный список
        """
        pass
