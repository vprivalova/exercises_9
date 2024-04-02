class NotSleeping:
    """
    A class representing the process of sheep counting before bedtime.

    Attributes:
        -

    Methods:
        add_sheep(number): Adding the sequence number of each new sheep to the list.
        lost(): Resetting the sheep count to zero.
        get_count_sheep(): Determining the number of sheep counted currently.
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

    @staticmethod
    def lost():
        """
        Resetting the sheep count to zero.
        :return: None
        """
        NotSleeping.sheep.clear()

    @staticmethod
    def get_count_sheep():
        """
        Determining the number of sheep counted currently.
        :return: Number of counted sheep.
        :rtype: int
        """
        return len(NotSleeping.sheep)


person1 = NotSleeping()

person1.add_sheep(1)
person1.add_sheep(2)
person1.add_sheep(3)
person1.add_sheep(4)
person1.add_sheep(5)
person1.lost()
person1.add_sheep(1)
person1.add_sheep(2)

print(person1.get_count_sheep())
