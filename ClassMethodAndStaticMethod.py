class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(f'{self.name} is running')

    def speak(self):
        print(f'My name is {self.name} and I am {self.age} years old')

    @classmethod
    def walk(cls):
        print('Player is walking')

    #class method can create instance of the class, and can be called from the class itself
    @classmethod
    def player_from_string(cls, string):
        name, age = string.split(',')
        return cls(name, age)

    #static method can't create instance of the class, and can be called from the class itself
    @staticmethod
    def talk():
        print('Player is talking')

player1 = Player.player_from_string('Tom,22')

player1.run()
player1.speak()

Player.walk()
Player.talk()


player2 = Player('Jerry', 21)
#class method or static method can be called from the instance of the class
player2.walk()