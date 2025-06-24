import os.path
from abc import ABC, abstractmethod


class FileHandler(ABC):

    def __init__(self, filename):
        self.__filename = filename

    @abstractmethod
    def get_vacancies(self, **kwargs):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy_id):
        pass

    @abstractmethod
    def update_vacancy(self, vacancies):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_id):
        pass



class JsonFileHandler(FileHandler):

    def __init__(self, filename):
        filename = 'data/vacancies.json'
        super().__init__(filename)


    def get_vacancies(self, **kwargs):
        try:
            with open(self._FileHandler__filename, 'r') as file:
                vacancies == json.load(file)
        except:

        if not os.path.exists(self._FileHandler__filename):
            return []
