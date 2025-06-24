from src.vacancies import Vacancy
from typing import Any, List, Dict



def vacancy_to_dict(vacancy: Vacancy) -> dict:
    """Метод преобразует объект Vacancy в словарь"""
    return {
        "title": vacancy.get_title,
        "url": vacancy.get_url,
        "salary": vacancy.get_salary,
        "description": vacancy.get_description
    }

def dict_to_vacancy(data: Dict[str, Any]) -> Vacancy:
    """Метод преобразует словарь в объект Vacancy"""
    return Vacancy(
        title = data.get("title"),
        url = data.get("url"),
        salary = data.get("salary"),
        description = data.get("description")
    )



def cast_to_object_list(data: List[Dict[str, Any]]) -> List[Vacancy]:
    """Метод преобразующий список словарей в список объектов класса Vacancy"""
    return [dict_to_vacancy(item) for item in data if isinstance(item, dict)]
