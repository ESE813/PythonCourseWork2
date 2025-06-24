from src.hh_api import HeadHunterAPI
from src.vacancies import Vacancy
from src.file_saver import JSONSaver
from src.user_interaction import user_interaction


# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI()

# Получение вакансий с hh.ru в формате JSON
hh_vacancies = hh_api.get_vacancies("Python")


# Пример работы конструктора класса с одной вакансией
vacancy = Vacancy(
    "Python Developer",
    "<https://hh.ru/vacancy/123456>",
    100000,
    "Требования: опыт работы от 3 лет...",
)

# Сохранение информации о вакансиях в файл
json_saver = JSONSaver()
json_saver.add_vacancy(vacancy)
json_saver.delete_vacancy(vacancy)


if __name__ == "__main__":
    user_interaction()
