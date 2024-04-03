class User:
    """
    A class representing a web-site user.

    Attributes:
        id (int): id number of the user.
        nick_name (str): Nickname of the user.
        first_name (str): First name of the user.
        last_name (str): Last name of the user.
        middle_name (str): Middle name of the user.
        gender (str): Gender of the user.

    Methods:
        update(id_new, nick_name_new, first_name_new, last_name_new=None, middle_name_new=None, gender_new=None):
            Updating some attributes of the original user information.
    """
    def __init__(self, id, nick_name, first_name, last_name=None, middle_name=None, gender=None):
        """
        Initializes a User object.

        :param id: id number of the user.
        :type id: int
        :param nick_name: Nickname of the user.
        :type nick_name: str
        :param first_name: First name of the user.
        :type first_name: str
        :param last_name: Last name of the user.
        :type last_name: str
        :param middle_name: Middle name of the user.
        :type middle_name: str
        :param gender: Gender of the user.
        :type gender: str
        """
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def update(self, id_new, nick_name_new, first_name_new, last_name_new=None, middle_name_new=None, gender_new=None):
        """
        Updating some attributes of the original user information.

        :param id_new: New id number of the user.
        :type id_new: int
        :param nick_name_new: New nickname of the user.
        :type nick_name_new: str
        :param first_name_new: New first name of the user.
        :type first_name_new: str
        :param last_name_new: New last name of the user.
        :type last_name_new: str
        :param middle_name_new: New middle name of the user.
        :type middle_name_new: str
        :param gender_new: New gender of the user.
        :type gender_new: str
        :return: None
        """
        if self.id != id_new:
            print('Аттрибут id не подлежит обновлению.')

        self.nick_name = nick_name_new
        self.first_name = first_name_new
        self.last_name = last_name_new
        self.middle_name = middle_name_new

        if self.gender != gender_new:
            print('Аттрибут gender не подлежит обновлению.')

    def __str__(self):
        return (f'User ID:{self.id}, Nickname: {self.nick_name}, Gender: {self.gender}, First name: {self.first_name}, '
                f'Middle Name: {self.middle_name}, Last name: {self.last_name}')

    def __repr__(self):
        return (f'{self.__class__} ID:{self.id}, Nickname: {self.nick_name}, Gender: {self.gender}, First name: {self.first_name}, '
                f'Middle Name: {self.middle_name}, Last name: {self.last_name}')


user1 = User(67890, 'John2005', 'John', 'Wilson')
user1.update(987, 'John2005', 'John', 'Wwwilson')
user2 = User(54, 'Peter578363', 'Peter')
print(str(user1))
print(repr(user1))
print(repr(user2))
