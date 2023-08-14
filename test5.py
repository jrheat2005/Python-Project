
# parent class
class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = 0
    arms = 0
    dna = "Sequence A"
    origin = "Unknown"
    carbon_based = True


    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg
# child class
class Human(Organism):
    name = 'Macguyver'
    species = 'Homosapien'
    legs = 2
    arms = 2
    origin = 'Earth'

    def ingenuity(self):
        msg = "\nCreates a deadly weapon using only a paper clip, chewing gum, and a roll of duct tape!"
        return msg
    
# child class
class Dog(Organism):
    name = 'Spot'
    species = 'Canine'
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = 'Earth'

    def bite(self):
            msg = "\nEmits a loud, menacing growl and bites down freociously on it's target!"
            return msg

# child class
class bacterium(Organism):
    name = 'X'
    species = 'Bateria'
    legs = 0
    arms = 0
    dna = "Sequence C"
    origin = 'Mars'

    def replication(self):
        msg = "\nThe cells begin to divide and multiply into two seperate organisms!"
        return msg


if __name__ == "__main__":
    human = Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bite())

    bacteria = bacterium()
    print(bacteria.information())
    print(bacteria.replication())
