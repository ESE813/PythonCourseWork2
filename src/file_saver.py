import os.path
import json
from abc import ABC, abstractmethod
from typing import List
from src.utils import vacancy_to_dict, dict_to_vacancy
from src.vacancies import Vacancy


class VacancySave(ABC):
    """Базовый класс для хранения вакансий"""

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        """Метод добавления вакансии в хранилище"""
        pass

    @abstractmethod
    def get_vacancy(self, **kwargs) -> List[Vacancy]:
        """Метод получения списка вакансий по критериям"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy):
        """Метод удаления вакансий с хранилища"""
        pass


class JSONSaver(VacancySave, ABC):
    def __init__(self, filename: str = "vacancies.json"):
        self.__filename =filename
        if not os.path.exists(self.__filename):
            with open(self.__filename, 'w') as f:
                json.dump([], f)


    def add_vacancy(self, vacancy: Vacancy):
        data = self._read_data()
        vacancy_dict = vacancy_to_dict(vacancy)
        if vacancy_dict not in data:
            data.append(vacancy_dict)
            self._write_data(data)

    def _read_data(self):
        with open(self.__filename, 'r') as f:
            return json.load(f)

    def _write_data(self, data):
        with open(self.__filename, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)



    def get_vacancy(self, **kwargs) -> List[Vacancy]:
        data = self._read_data()
        return [
            dict_to_vacancy(item)
            for item in data if all(str(item.get(k)).lower() == str(v).lower()
                                    for k, v in kwargs.items())
        ]


    def delete_vacancy(self, vacancy: Vacancy):
        data = self._read_data()
        update_data = [i for i in data if not (i["title"] == vacancy.get_title and i["url"] == vacancy.get_url)]
        self._write_data(update_data)

