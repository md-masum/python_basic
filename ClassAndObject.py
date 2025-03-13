class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(f'{self.name} is running')

    def speak(self):
        print(f'My name is {self.name} and I am {self.age} years old')



player1 = Player('Tom', 22)
player2 = Player('Jerry', 21)

player1.run()
player1.speak()
player2.run()
player2.speak()