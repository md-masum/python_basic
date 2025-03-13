class Player:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login(self):
        if len(self.email) > 0 and len(self.password) > 0:
            print('Player logged in')
        else:
            print('Player not logged in')


class Wizard(Player):  # Inheriting from Player class
    def __init__(self, email, password, name, power):
        super().__init__(email, password)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name} is running')

    def attack(self):
        print(f'Player {self.name} is attacking with power {self.power}')


class Archer(Player):  # Inheriting from Player class
    def __init__(self, email, password, name, arrow_count):
        super().__init__(email, password)
        self.name = name
        self.arrow_count = arrow_count

    def run(self):
        print(f'{self.name} is running')

    def attack(self):
        print(f'Player {self.name} is attacking with Arrow {self.arrow_count}')


class SuperPlayer(Wizard, Archer):  # Multiple inheritance
    def __init__(self, email, password, name, power, arrow_count):
        # Initialize Player (Base class)
        Player.__init__(self, email, password)
        
        # Initialize attributes from both Wizard and Archer
        self.name = name
        self.power = power
        self.arrow_count = arrow_count

    def special_attack(self):
        print(f'{self.name} is using a special attack with power {self.power} and arrows {self.arrow_count}')


# Testing the classes
wizard1 = Wizard('tom@gmail.com', 'password', 'Tom', 50)
wizard1.login()
wizard1.run()
wizard1.attack()

print()
archer1 = Archer('jerry@gmail.com', 'Password', 'Jerry', 100)
archer1.login()  # This will work because Archer class is inheriting from Player class
archer1.run()
archer1.attack()



print()
# Testing SuperPlayer class
super_player = SuperPlayer('superuser@gmail.com', 'superpass', 'superuser', 80, 150)
super_player.login()  # Inherited from Player
super_player.run()  # Inherited from Wizard/Archer
super_player.attack()  # Inherited from Wizard (MRO applies)
super_player.special_attack()  # Unique to SuperPlayer



print()
# isinstance() is used to check if an object is an instance of a class
print(isinstance(wizard1, Wizard)) #True
print(isinstance(wizard1, Player)) #True
print(isinstance(wizard1, object)) #True
print(isinstance(wizard1, Archer)) #False
print(isinstance(wizard1, SuperPlayer)) #False
print(isinstance(super_player, SuperPlayer)) #True
print(isinstance(super_player, Wizard)) #True
print(isinstance(super_player, Archer)) #True
print(isinstance(super_player, Player)) #True