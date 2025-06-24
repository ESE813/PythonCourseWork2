import pytest
from src.vacancies import Vacancy
from src.utils import vacancy_to_dict, dict_to_vacancy


@pytest.fixture
def sample_vacancy():
    return Vacancy(
        title="Python Developer",
        url="https://api.hh.ru/vacancies",
        salary=150000,
        description="Опыт с Django",
    )


@pytest.fixture
def sample_dict():
    return {
        "title": "Python Developer",
        "url": "https://api.hh.ru/vacancies",
        "salary": 150000,
        "description": "Опыт с Django",
    }


def test_vacancy_to_dict(sample_vacancy, sample_dict):
    result = vacancy_to_dict(sample_vacancy)
    assert result == sample_dict


def test_dict_to_vacancy(sample_dict):
    vacancy = dict_to_vacancy(sample_dict)
    assert isinstance(vacancy, Vacancy)
    assert vacancy.get_title == "Python Developer"
    assert vacancy.get_url == "https://api.hh.ru/vacancies"
    assert vacancy.get_salary == 150000
    assert vacancy.get_description == "Опыт с Django"

