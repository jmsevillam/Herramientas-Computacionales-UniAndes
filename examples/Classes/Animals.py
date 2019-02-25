# This code was written during the course
# "Herramientas computacionales" at Uniandes
# Mauricio Sevilla. email: j.sevillam@uniandes.edu.co

#This class can create animals and give them some orders
class animals:
    def __init__(self,name,spe,age,talk):
        self.name=name #We save the name
        self.spe=spe   #We save which animal it is
        self.age=age   #We save the age.
        self.speech=talk # We save what the animal says
    #Method definitions
    def talk(self): 
        print(self.speech) # Prints the speech of the animal
    def sit(self): #If dog, sits, neehh if other
        if self.spe=='Dog':
            print('Sitted!')
        else:
            print('Nehh!!')
    #One year passes
    def year_pass(self):
        self.age+=1
#Create a zoo (A list where we save the animals)
Zoo=[]
Zoo.append(animals('Scooby','Dog',1,'Woof')) #Create a dog named Scooby
#Say to dog: talk
Zoo[0].talk()
#create a cat
Zoo.append(animals('Tom','Cat',1,'Miau'))
#Ask the cat to sit
Zoo[1].sit()
#ask the dog to sit
Zoo[0].sit()
#Ask cat's age
print(Zoo[1].age)
#one year passes
Zoo[1].year_pass()
#ask cat's age
print(Zoo[1].age)
