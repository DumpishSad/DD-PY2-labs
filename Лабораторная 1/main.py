# TODO Написать 3 класса с документацией и аннотацией типов
class Transport:
    def __init__(self, brand: str, model: str, year: int):
        """
        Создает объект транспортного средства.

        :param brand: Марка транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.
        """
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self) -> str:
        """
        Запускает двигатель транспортного средства.

        :return: Строка с сообщением о запуске двигателя.

        >>> car = Transport("Toyota", "Camry", 2022)
        >>> car.start_engine()
        'Двигатель машины Toyota Camry запущен.'
        """
        return f'Двигатель машины {self.brand} {self.model} запущен.'

    def drive(self, distance: float) -> str:
        """
        Осуществляет поездку на заданное расстояние.

        :param distance: Расстояние в километрах.
        :return: Строка с сообщением о поездке.

        >>> bike = Transport("Harley-Davidson", "Sportster", 2021)
        >>> bike.drive(50.5)
        'Проехали 50.5 км на Harley-Davidson Sportster.'
        """
        return f'Проехали {distance} км на {self.brand} {self.model}.'

    def stop_engine(self) -> str:
        """
        Останавливает двигатель транспортного средства.

        :return: Строка с сообщением об остановке двигателя.

        >>> bus = Transport("Mercedes-Benz", "Sprinter", 2020)
        >>> bus.stop_engine()
        'Двигатель Mercedes-Benz Sprinter остановлен.'
        """
        return f'Двигатель {self.brand} {self.model} остановлен.'


class Book:
    def __init__(self, title: str, author: str, genre: str, year_published: int):
        """
        Создает объект книги.

        :param title: Название книги.
        :param author: Автор книги.
        :param genre: Жанр книги.
        :param year_published: Год публикации книги.
        """
        self.title = title
        self.author = author
        self.genre = genre
        self.year_published = year_published

    def read_book(self) -> str:
        """
        Позволяет прочитать книгу.

        :return: Строка с сообщением о прочтении книги.

        >>> novel = Book("Crime and Punishment", "Fyodor Dostoevsky", "Fiction", 1866)
        >>> novel.read_book()
        'Чтение книги "Crime and Punishment" автора Fyodor Dostoevsky.'
        """
        return f'Чтение книги "{self.title}" автора {self.author}.'

    def recommend_book(self, friend: str) -> str:
        """
        Рекомендует книгу другу.

        :param friend: Имя друга.
        :return: Строка с рекомендацией.

        >>> mystery_book = Book("The Da Vinci Code", "Dan Brown", "Mystery", 2003)
        >>> mystery_book.recommend_book("Alice")
        'Рекомендую прочитать книгу "The Da Vinci Code" автора Dan Brown, Alice.'
        """
        return f'Рекомендую прочитать книгу "{self.title}" автора {self.author}, {friend}.'

    def get_genre(self) -> str:
        """
        Возвращает жанр книги.

        :return: Жанр книги.

        >>> sci_fi_book = Book("Dune", "Frank Herbert", "Science Fiction", 1965)
        >>> sci_fi_book.get_genre()
        'Science Fiction'
        """
        return self.genre


class BankAccount:
    def __init__(self, account_holder: str, balance: float = 0.0):
        """
        Создает объект банковского счета.

        :param account_holder: Владелец счета.
        :param balance: Начальный баланс счета (по умолчанию 0).
        """
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount: float) -> str:
        """
        Пополняет банковский счет.

        :param amount: Сумма для пополнения.
        :return: Строка с подтверждением пополнения.

        >>> savings_account = BankAccount("John Doe", 500.0)
        >>> savings_account.deposit(100.0)
        'Счет владельца John Doe пополнен на 100.0 рублей. Текущий баланс: 600.0 рублей.'
        """
        self.balance += amount
        return f'Счет владельца {self.account_holder} пополнен на {amount} рублей. Текущий баланс: {self.balance} рублей.'

    def withdraw(self, amount: float) -> str:
        """
        Снимает средства с банковского счета.

        :param amount: Сумма для снятия.
        :return: Строка с подтверждением снятия средств.

        >>> checking_account = BankAccount("Alice Smith", 1000.0)
        >>> checking_account.withdraw(200.0)
        'Со счета владельца Alice Smith снято 200.0 рублей. Текущий баланс: 800.0 рублей.'
        """
        if amount > self.balance:
            return 'Недостаточно средств на счете.'
        self.balance -= amount
        return f'Со счета владельца {self.account_holder} снято {amount} рублей. Текущий баланс: {self.balance} рублей.'

    def get_balance(self) -> float:
        """
        Возвращает текущий баланс счета.

        :return: Текущий баланс счета.

        >>> account = BankAccount("Jane Doe", 1500.0)
        >>> account.get_balance()
        1500.0
        """
        return self.balance


if __name__ == "__main__":
    import doctest
    doctest.testmod()
