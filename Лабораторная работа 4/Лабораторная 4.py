# noinspection SpellCheckingInspection
class Transport:
    """Базовый класс для транспортных средств."""

    def __init__(self, brand: str, model: str, year: int):
        """
        Конструктор класса.

        :param brand: Марка транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.
        """
        # проверка на корректность введенного года
        if not isinstance(year, int) or year < 0 or year > 2023:
            raise ValueError("Год введён неверно!")
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self) -> str:
        """
        Возвращает строковое представление транспортного средства.

        :return: Строковое представление транспортного средства.
        """
        return f"{self.brand} {self.model} ({self.year})"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление транспортного средства.

        :return: Формальное строковое представление транспортного средства.
        """
        return f"Transport(brand={self.brand}, model={self.model}, year={self.year})"


# noinspection SpellCheckingInspection
class Car(Transport):
    """Дочерний класс для класса транспорт."""

    def __init__(self, brand: str, model: str, year: int, num_doors: int):
        """
        Конструктор класса.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        :param num_doors: Количество дверей в автомобиле.
        """
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def start_engine(self) -> str:
        """
        Запускает двигатель автомобиля.

        :return: Сообщение о запуске двигателя.
        """
        return f"{self.brand} {self.model} двигатель запущен."

    def __str__(self) -> str:
        """
        Возвращает строковое представление легкового автомобиля.

        :return: Строковое представление легкового автомобиля.
        """
        return f"{super().__str__()}, {self.num_doors} дверей"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление легкового автомобиля.

        :return: Формальное строковое представление легкового автомобиля.
        """
        return f"Car(brand={self.brand}, model={self.model}, year={self.year}, num_doors={self.num_doors})"


# noinspection SpellCheckingInspection
class DriftCar(Car):
    """Дочерний класс для класса легковые машины."""

    def __init__(self, brand: str, model: str, year: int, num_doors: int, hydraulic_arm: bool, blocking_dif: bool):
        """
        Конструктор класса.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        :param num_doors: Количество дверей в автомобиле.
        :hydraulic_arm: Наличие гидроручнирка
        :blocking_dif: Наличие блокировки диффренциала
        """
        super().__init__(brand, model, year, num_doors)
        self.hydraulic_arm = hydraulic_arm
        self.blocking_dif = blocking_dif

    def __str__(self) -> str:
        """
        Возвращает строковое представление дрифт автомобиля.

        :return: Строковое представление дрифт автомобиля.
        """
        return f"{super().__str__()}, гидроручник - {self.hydraulic_arm}, заварка - {self.blocking_dif}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление дрифт автомобиля.

        :return: Формальное строковое представление дрифт автомобиля.
        """
        return f"DriftCar(brand={self.brand}, model={self.model}, year={self.year}, num_doors={self.num_doors}, " \
               f"hydraulic_arm={self.hydraulic_arm}, blocking_dif={self.blocking_dif})"

    def drift(self) -> str:
        """
        Запускает режим опасного вождения.

        :return: Сообщение о запуске режима опасного вождения.
        """
        return f"DriftCar(model={self.model}) дал угла"


# noinspection SpellCheckingInspection
if __name__ == "__main__":
    # Создаем экземпляр базового класса Transport
    transport_vehicle = Transport(brand="Toyota", model="Camry", year=2022)

    # Выводим информацию о транспортном средстве с использованием __str__
    print(str(transport_vehicle))

    # Выводим формальное представление транспортного средства с использованием __repr__
    print(repr(transport_vehicle))

    # Создаем экземпляр дочернего класса Car
    car_vehicle = Car(brand="Tesla", model="Model 3", year=2023, num_doors=4)

    # Выводим информацию о легковом автомобиле
    print(str(car_vehicle))

    # Выводим формальное представление легкового автомобиля
    print(repr(car_vehicle))

    # Запускаем двигатель легкового автомобиля
    engine_start_message = car_vehicle.start_engine()
    print(engine_start_message)

    # Создаем экземпляр дочернего класса DriftCar
    drift_car = DriftCar(brand="ВАЗ", model="Шаха", year=1976, num_doors=4, hydraulic_arm=True, blocking_dif=True)

    # Выводим информацию о дрифт автомобиле с использованием __str__
    print(str(drift_car))

    # Выводим формальное представление дрифт автомобиля с использованием __repr__
    print(repr(drift_car))

    # Включаем режим опасного вождения
    drift_start = drift_car.drift()
    print(drift_start)
