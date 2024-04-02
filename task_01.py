class Dog:
    """
    A class representing the dog.

    Attributes:
        name (str): The name of the dog.
        breed (str): The breed of the dog.
        color (str): The color of the dog's fur.
        age (int): The age of the dog.

    Methods:
        say(): Printing the sound of a dog barking.
    """
    def __init__(self, name, breed, color, age):
        """
        Initializes a Dog object.

        :param name: The name of the dog.
        :type name: str

        :param breed: The breed of the dog.
        :type breed: str

        :param color: The color of the dog's fur.
        :type color: str

        :param age: The age of the dog.
        :type age: int
        """
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age

    @staticmethod
    def say():
        """
        Printing the sound of a dog barking.

        :return: None
        """
        print('Гав!')


dog1 = Dog('Шарик', 'лабрадор', 'золотистый', 7)
dog1.say()
