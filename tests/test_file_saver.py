import os
import json
import pytest
from src.vacancies import Vacancy
from src.file_saver import JSONSaver
from src.utils import vacancy_to_dict


@pytest.fixture
def temp_json_file(tmp_path):
    file_path = tmp_path / "test_vacancies.json"
    return str(file_path)


@pytest.fixture
def test_vacancy():
    return Vacancy("Test Dev", "https://example.com", 90000, "Some description")


def test_json_saver_init_creates_file(temp_json_file):
    saver = JSONSaver()
    saver.__init__(temp_json_file)

    assert os.path.exists(temp_json_file)
    with open(temp_json_file, "r") as f:
        assert json.load(f) == []


def test_add_vacancy(temp_json_file, test_vacancy):
    saver = JSONSaver()
    saver.__init__(temp_json_file)

    saver.add_vacancy(test_vacancy)

    with open(temp_json_file, "r") as f:
        data = json.load(f)
        assert len(data) == 1
        assert data[0] == vacancy_to_dict(test_vacancy)


def test_get_vacancy(temp_json_file, test_vacancy):
    saver = JSONSaver()
    saver.__init__(temp_json_file)
    saver.add_vacancy(test_vacancy)

    results = saver.get_vacancy(title="Test Dev")
    assert len(results) == 1
    assert isinstance(results[0], Vacancy)
    assert results[0].get_url == "https://example.com"


def test_delete_vacancy(temp_json_file, test_vacancy):
    saver = JSONSaver()
    saver.__init__(temp_json_file)
    saver.add_vacancy(test_vacancy)

    data_before = saver._read_data()
    assert len(data_before) == 1

    saver.delete_vacancy(test_vacancy)

    data_after = saver._read_data()
    assert len(data_after) == 0
