from typing import Any

import requests
from abc import ABC, abstractmethod
from src.vacancies import Vacancy




class Parser(ABC):
    """Абстрактный класс для работы с API"""

    def __init__(self):
        self._base_url = None

    @abstractmethod
    def _connect(self, params: dict) -> dict:
        """Метод для подключения к API"""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str, page: int = 0, per_page: int = 50) -> list:
        """Метод для получения вакансий по ключевому слову"""
        pass


class HeadHunterAPI(Parser):

    def __init__(self):
        super().__init__()
        self._base_url = "https://api.hh.ru/vacancies"


    def _connect(self, params: dict) -> dict:

        response = requests.get(self._base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Ошибка при подключении к HH API: {response.status_code}")


    def get_vacancies(self, keyword: str, page: int = 0, per_page: int = 50) -> list[dict[str, Any]]:

        params = {
            "text": keyword,
            "page": page,
            "per_page": per_page
        }
        data = self._connect(params)
        vacancies = []

        for item in data.get("items", []):
            vacancies.append({
            "title": item.get("name"),
            "url": item.get("url"),
            "salary": item.get("salary", None),
            "description": item.get("snippet", {}).get("requirement", "")
        })

        return vacancies