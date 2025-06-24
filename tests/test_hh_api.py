from unittest.mock import patch

from src.hh_api import HeadHunterAPI


@patch.object(HeadHunterAPI, "_connect")
def test_get_vacancies(mock_connect):
    mock_connect.return_value = {
        "items": [
            {
                "name": "Python Developer",
                "url": "https://hh.ru/vacancy/123",
                "salary": {"from": 100000, "to": 150000},
                "snippet": {"requirement": "Опыт с Python"},
            }
        ]
    }

    api = HeadHunterAPI()
    vacancies = api.get_vacancies("Python")

    assert isinstance(vacancies, list)
    assert len(vacancies) == 1
    assert vacancies[0]["title"] == "Python Developer"
    assert vacancies[0]["url"] == "https://hh.ru/vacancy/123"
    assert vacancies[0]["salary"] == {"from": 100000, "to": 150000}
    assert "Python" in vacancies[0]["description"]
