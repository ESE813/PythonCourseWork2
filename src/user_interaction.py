from typing import List

from src.vacancies import Vacancy
from src.file_saver import JSONSaver
from src.hh_api import HeadHunterAPI
from src.utils import cast_to_object_list


def filter_vacancies(vacancies: List[Vacancy], keyword: str) -> list:
    """Фильтрует вакансии по ключевому слову"""
    return [
        vacancy for vacancy in vacancies if any(word.lower() in vacancy.get_description.lower()
                                                for word in keyword)
    ]


def get_vacancies_by_salary(vacancies: List[Vacancy], salary_range: str) -> list:
    """Фильтрует вакансии по диапазону зарплаты"""
    try:
        min_salary, max_salary = map(int, salary_range.replace(" ", "").split("-"))
    except ValueError:
        print("Неверный диапазон зарплаты")
        return vacancies
    return [vacancy for vacancy in vacancies if min_salary <= vacancy.get_salary <= max_salary]



def sort_vacancies(vacancies: List[Vacancy]) -> list:
    """Сортирует вакансии по зарплате"""
    return sorted(vacancies, key=lambda vacancy: vacancy.get_salary, reverse=True)



def get_top_vacancies(vacancies: List[Vacancy], top_n: int) -> list:
    """Возвращает топ N вакансий"""
    return vacancies[:top_n]



def print_vacancies(vacancies: List[Vacancy]):
    """Печатает в консоль список вакансий"""
    if not vacancies:
        print("Нет подходящих вакансий")
    for vacancy in vacancies:
        print(f"Вакансия: {vacancy.get_title}. Зарплата: {vacancy.get_salary}")
        print(f"Ссылка на вакансию: {vacancy.get_url}")
        print(f"Описание вакансии: {vacancy.get_description}")


def user_interaction():

    search_query = input("Введите поисковый запрос: ").strip()
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    keyword = str(input("Введите ключевое слово для фильтрации вакансий: ").split())
    salary_range = input("Введите диапазон зарплат: ") # Пример: 100000 - 150000

    api = HeadHunterAPI()
    api_data = api.get_vacancies(search_query)
    vacancies_list = cast_to_object_list(api_data)

    filtered_vacancies = filter_vacancies(vacancies_list, keyword)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)



