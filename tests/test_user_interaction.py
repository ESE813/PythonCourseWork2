import pytest
from src.vacancies import Vacancy
from src.user_interaction import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies


@pytest.fixture
def vacancies():
    return [
        Vacancy(
            "Python Dev",
            "https://api.hh.ru/vacancies",
            120000,
            "Опыт работы с Python и Django",
        ),
        Vacancy(
            "Java Dev", "https://api.hh.ru/vacancies", 100000, "Spring Framework, Java"
        ),
        Vacancy(
            "Frontend Dev", "https://api.hh.ru/vacancies", 90000, "React, JavaScript"
        ),
        Vacancy("Intern", "https://api.hh.ru/vacancies", None, "Стажировка без опыта"),
    ]


def test_filter_vacancies(vacancies):
    filtered = filter_vacancies(vacancies, keyword="python")
    assert len(filtered) == 3
    assert filtered[0].get_title == "Python Dev"


def test_get_vacancies_by_salary_valid_range(vacancies):
    filtered = get_vacancies_by_salary(vacancies, "100000 - 150000")
    assert len(filtered) == 2
    assert all(95000 <= v.get_salary <= 130000 for v in filtered)


def test_get_vacancies_by_salary_invalid_range(vacancies):
    filtered = get_vacancies_by_salary(vacancies, "abc - 10000")
    assert filtered == vacancies


def test_sort_vacancies(vacancies):
    sorted_list = sort_vacancies(vacancies)
    salaries = [v.get_salary for v in sorted_list]
    assert salaries == sorted(salaries, reverse=True)


def test_get_top_vacancies(vacancies):
    sorted_list = sort_vacancies(vacancies)
    top = get_top_vacancies(sorted_list, 2)
    assert len(top) == 2
    assert top[0].get_salary >= top[1].get_salary

