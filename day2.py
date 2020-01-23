
# inheritance

# Writer is the superclass
# class Writer:
#     num_writers=0
#     Best_writer='albert camus'
#
#     def __init__(self, name, n_books):
#         self.name=name
#         self.n_books =n_books
#         Writer.num_writers += 1
#
#     def write(self):
#         self.n_books += 1
#
#     @staticmethod
#     def be_honest():
#         print(Writer.Best_writer + " is the best")
#
#
#
# # philosopher is a child of Writer
# class Philosopher(Writer):
#     Best= 'Niezctche'
#
#     def write_nonsense(self):
#         print(f'This is complete nonsense, {self.name}')
#         self.write()
#
#     @staticmethod
#     def be_honest():
#         print(Philosopher.Best +' is the best philosopher')
#
#
# class French:
#     def __init__(self, name, ):
#         self.name = name
#
#
#     def talk_nonsense(self):
#         print(f"complete nonsense {self.name}")
#
#
# # a class can have multiple parents
# class FrenchThinker(Philosopher, French):
#
#     def postmodern_nonsense(self):
#         print("postmodern bs")
#
#
#
# if __name__== "__main__":
#     sun_tzu = Writer(name="Sun Tzu", n_books=1)
#     print(sun_tzu.n_books)
#     sun_tzu.be_honest()
#     Kant = Philosopher(name= 'Emmanuel Kant', n_books =20)
#     print(Kant.name, Kant.n_books)
#     Kant.write()
#     print(Kant.n_books)
#     Kant.be_honest()
#     jaques = French(name='Jaques' )
#     jaques.talk_nonsense()
#     Derrida = FrenchThinker(name="Jacques Derrida", n_books=50)
#     Derrida.talk_nonsense()
#     Derrida.postmodern_nonsense()
#     Derrida.write()
#     print(f'{Derrida.name} wrote {Derrida.n_books} of complete nonsense')



# Excercise 1
#
# class Family:
#     def __init__(self, last_name, members):
#         self.members = members
#         self.last_name = last_name
#
#     def born(self, **kwargs):
#         child = {**kwargs}
#         self.members.append(child)
#         print(f"Mazal Tov a new baby {child.get('sex')} was born named {child.get('name')} {self.last_name}")
#
#
#
#     def is_18(self):
#         for i in range(len(self.members)):
#             if self.members[i].get('is_child') == True:
#                 if self.members[i].get('age') >=18:
#                     print(f"{self.members[i].get('name')} you are {self.members[i].get('age')} years old, get a job")
#                 else:
#                     print(f"{self.members[i].get('name')} you are {self.members[i].get('age')} years old, continue your work at the sweat shop making shoes")
#
#
# the_family =Family("Christ", [{'name':'Michael','age':35,'sex':'Male','is_child':False},
#     {'name':'Sarah','age':32,'sex':'Female','is_child':False},
#     {'name':'Kevin','age':16,'sex':'Male','is_child':True}])
#
# print(the_family.members)
#
#
# unBornChildrenToAdd=[{'name':'Hesus','age':0,'sex':'Male','is_child':True},
#     {'name':'Mary','age':3,'sex':'Female','is_child':True},
#     {'name':'Satan','age':5780,'sex':'Male','is_child':True}]
# for i in range(len(unBornChildrenToAdd)):
#     the_family.born(**unBornChildrenToAdd[i])
#
# the_family.is_18()


# Exercices XP Gold

import random
class Battle:
    def fight(self, listjedi, listsith):
        while len(listjedi) !=0 and len(listsith) !=0:
            jedi = random.choice(listjedi)
            sith = random.choice(listsith)
            if (2 / (((1 / jedi.power)) + (1 / jedi.wisdom))) > (2 / (((1 / sith.power)) + (1 / sith.wisdom))):
                print(f"{jedi.name}  defeated {sith.name}!")
                jedi.train()
                listsith.remove(sith)

            elif (2 / (((1 / jedi.power)) + (1 / jedi.wisdom))) == (2 / (((1 / sith.power)) + (1 / sith.wisdom))):
                print(f"the force is strong for both {jedi.name} and {sith.name}")
                jedi.train()
                sith.train()
            else:
                print(f"{sith.name} defeated {jedi.name}!")
                sith.train()
                listjedi.remove(jedi)

    def battle_result(self, listjedi, listsith):
        if not listjedi:
            print("The Sith control the Galaxy")
            for sith in listsith:
                print(sith.name)
        elif not listsith:
            print("the Jedi brought peace to the Galaxy!")
            for jedi in listjedi:
                print(jedi.name)







class ForceWielder:
    def __init__(self, name):
        self.name = name
        self.power = random.randint(1, 16)
        self.wisdom = random.randint(1, 16)

    def train(self):
        pass

    # do math final equation for harmonic method maybe as static method



    def is_jedi(self):
        pass


class Jedi(ForceWielder):
    def __init__(self, name):
        super().__init__(name)

        if self.power< self.wisdom:
            lightsaber_color = 'green'
        elif self.power == self.wisdom:
            lightsaber_color = 'purple'
            self.wisdom+=10 # teacher made all jedi get it not if have purple
        else:
            lightsaber_color = 'blue'

        self.lightsaber_color = lightsaber_color

    def train(self):
        self.wisdom += random.randint(10, 21)
        self.power += random.randint(5, 16)
        if self.wisdom >= 30:
            self.wisdom += 20
            print(f'{self.name} is now a Jedi Master. powerful in the force as Master Yoda!')
        elif self.power >= 27:
            self.power += 20
            print(f'{self.name} is now a Jedi Master, a master lightsaber duelist!')

    def is_jedi(self):
        return True

class Sith(ForceWielder):
    def __init__(self, name):
        super().__init__("Darth "+ name)
        self.lightsaber_color = "red"
        self.power += 10

    def train(self):
        self.wisdom += random.randint(5, 16)
        self.power += random.randint(10, 21)
        if self.wisdom >= 25:
            self.wisdom += 40
            print(f'{self.name} is as powerful as Lord Sidius with powerful force lightning!')
        elif self.power >= 30:
            self.power += 40
            print(f'{self.name} is now unstoppable, as Darth Vader with powerful force choke!')



    def is_jedi(self):
        return False


# the prep for battle

jedi_Fredrich = Jedi("Jedi Fredrich")
jedi_Raziel = Jedi("Jedi Raziel")
jedi_Chewbacca =Jedi("Jedi Chewbacca")
jedi_Yadger = Jedi("Jedi Yadger")
jedi_Jesus = Jedi("Jedi Jesus")

list_of_Jedi = [jedi_Fredrich, jedi_Raziel, jedi_Chewbacca, jedi_Yadger, jedi_Jesus]
for jedi in list_of_Jedi:
    print(f'{jedi.name} has entered the battlefield with {jedi.lightsaber_color} lightsaber')
    jedi.train()




sith_Yoni = Sith("Yoni")
sith_Ilan = Sith("Ilan")
sith_Thrawn = Sith("Thrawn")
sith_Jarjar = Sith("Jarjar")
sith_Satan = Sith("Satan")

list_of_Sith = [sith_Yoni, sith_Ilan, sith_Thrawn, sith_Jarjar, sith_Satan]
for sith in list_of_Sith:
    print(f'{sith.name} has entered the battlefield')
    sith.train()


# The Battle
battle = Battle()

battle.fight(list_of_Jedi, list_of_Sith)

battle.battle_result(list_of_Jedi, list_of_Sith)








