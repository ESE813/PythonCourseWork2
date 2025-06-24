
class Vacancy():

    def __init__(self, title: str, url: str, salary: int|None, description: str):
        self._title = title.strip()
        self._url = url.strip()
        self._salary = self._validate_salary(salary)
        self._description = description.strip()



    @staticmethod
    def _validate_salary(salary: int|None) -> int:
        """Метод проверки зарплаты"""
        if isinstance(salary, (int, float)) and salary > 0:
            return salary
        else:
            return 0

    @property
    def get_title(self):
        return self._title

    @property
    def get_url(self):
        return self._url

    @property
    def get_salary(self):
        return self._salary

    @property
    def get_description(self):
        return self._description

    @classmethod
    def cast_to_object_list(cls):





    def __lt__(self, other):
        if isinstance(other, Vacancy):
            return self._salary < other._salary
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, Vacancy):
            return self._salary <= other._salary
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Vacancy):
            return self._salary > other._salary
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Vacancy):
            return self._salary >= other._salary
        else:
            return NotImplemented

    def __repr__(self):
        salary_text = f"{self._salary}руб." if self._salary > 0 else "Зарплата не указана"
        return f"Vacancy('{self._title}', salary: {salary_text}, url: {self._url})"





