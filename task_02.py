class NotSleeping:
    """
    A class representing the process of sheep counting before bedtime.

    Attributes:
        sheep (list) - list of all sheep counted

    Methods:
        add_sheep(number): Adding the sequence number of each new sheep to the list.
    """

    sheep = []

    @staticmethod
    def add_sheep(number):
        """
        Adding the sequence number of each new sheep to the list.

        :param number : Sequence number of the new sheep.
        :type number: int

        :return: None
        """
        NotSleeping.sheep.append(number)


person1 = NotSleeping()
person1.add_sheep(1)
person1.add_sheep(2)
person1.add_sheep(3)
person1.add_sheep(4)
person1.add_sheep(5)

print(person1.sheep)
