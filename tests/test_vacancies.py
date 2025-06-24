import pytest
from src.vacancies import Vacancy



def test_vacancy_creation_valid_salary():
    v = Vacancy("Python Dev", "https://example.com", 120000, "Требуется опыт")
    assert v.get_title == "Python Dev"
    assert v.get_url == "https://example.com"
    assert v.get_salary == 120000
    assert v.get_description == "Требуется опыт"


def test_vacancy_creation_invalid_salary():
    v = Vacancy("Java Dev", "https://example.com", "неизвестно", "Без опыта")
    assert v.get_salary == 0


def test_salary_validation():
    assert Vacancy._validate_salary(100000) == 100000
    assert Vacancy._validate_salary(-5000) == 0
    assert Vacancy._validate_salary("100000") == 0
    assert Vacancy._validate_salary(None) == 0


def test_comparison_operators():
    v1 = Vacancy("A", "url", 50000, "desc")
    v2 = Vacancy("B", "url", 100000, "desc")

    assert v1 < v2
    assert v1 <= v2
    assert v2 > v1
    assert v2 >= v1


def test_repr_output():
    v1 = Vacancy("Django Dev", "https://example.com", 80000, "desc")
    assert (
        repr(v1) == "Vacancy('Django Dev', salary: 80000руб., url: https://example.com)"
    )

    v2 = Vacancy("Go Dev", "https://example.com", None, "desc")
    assert (
        repr(v2)
        == "Vacancy('Go Dev', salary: Зарплата не указана, url: https://example.com)"
    )
