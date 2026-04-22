from typing import Any

class BaseDBManager:
    """ Базовый класс для работ с базами данных. """
    def __init__(self, connection) -> None:
        """Метод - конструктор, для инициализации объектов класса."""
        self.conn = connection

    def get_info_countries_and_planes(self) -> list[dict[str, int]]:
        """ Метод для получения списка всех стран и количество самолётов в каждой стране. """
        pass

    def get_all_planes(self) -> list[dict[str, Any]]:
        """ Метод для получения списка всех самолётов с указанием страны регистрации,
         номера самолёта, скорость полёта и высота полёта. """
        pass

    def get_avg_height(self) -> float:
        """ Метод для получения средней высоты полёта всех самолётов. """
        pass

    def get_max_height(self):
        """ Метод для получения списка всех самолётов, у которых высота полёта выше средней по всем самолётам. """
        pass

    def get_planes_by_countries(self, list_country: list[str]):
        """ Метод получает список всех самолётов, зарегистрированных в странах
         названия которых переданы в метод, например (Iran, Russia). """
        pass

