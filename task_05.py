class Game:
    scoring = [0, 0]

    def __init__(self, name1, name2):
        self.commands = {'command1': name1, 'command2': name2}

    @staticmethod
    def ball_thrown(command, points):
        if command == 1:
            Game.scoring[0] += points
        else:
            Game.scoring[1] += points

    @staticmethod
    def get_score():
        return tuple(Game.scoring)

    def get_winner(self):
        if Game.scoring[0] > Game.scoring[1]:
            return self.commands['command1']
        elif Game.scoring[0] < Game.scoring[1]:
            return self.commands['command2']
        else:
            return 'Ничья'


game1 = Game('БК Сибирь', 'БК Нижний Новгород')
game1.ball_thrown(1, 30)
game1.ball_thrown(1, 15)
print(game1.get_score())
game1.ball_thrown(2, 30)
print(game1.get_winner())
