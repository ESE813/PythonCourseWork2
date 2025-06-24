import requests
import json
from abc import ABC, abstractmethod

class Parser(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def get_vacancies(self,name: str, url: str,  text: str, page: int = 0, per_page: int = 50) -> list:
        """Метод для получения вакансий по ключевому слову"""
        pass


class HeadHunterAPI(Parser):
    BASE_URL = "https://api.hh.ru/vacancies"

    def get_vacancies(self,name: str, url: str,  text: str, page: int = 0, per_page: int = 50) -> list:
        params = {
            "name": name,
            "alternate_url": url,
            "text": text,
            "page": page,
            "per_page": per_page
        }
        response = requests.get(self.BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            return data.get("items", [])
        else:
            raise Exception(f"Ошибка при подключении к HH API: {response.status_code}")