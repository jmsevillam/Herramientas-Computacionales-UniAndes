import random
class vehicle:
    def __init__(self,Color,Wheels,MaxVel):
        self.Color=Color
        self.Wheels=Wheels
        self.VMax=MaxVel
    def Move(self):
        v=random.random()*self.VMax
        print('The velocity is: '+str(v))
    def Park(self):
        print('The vehicle is parked')


class Bicycle(vehicle):
    def __init__(self,Color,Wheels,MaxVel):
        vehicle.__init__(self,Color,Wheels,MaxVel)
    def Do_some_exercise(self):
        print('Doing exercise')

class Motorcycle(vehicle):
    def __init__(self,Color,Wheels,MaxVel):
        vehicle.__init__(self,Color,Wheels,MaxVel)
    def Put_Helmet(self):
        print("Helmet's on")

class Car(vehicle):
    def __init__(self,Color,Wheels,MaxVel):
        vehicle.__init__(self,Color,Wheels,MaxVel)
    def Turn_on_Radio(self):
        print("Radio's on")

        
b=Bicycle('Red',2,10)
print(b.Color)
b.Do_some_exercise()
b.Move()
b.Park()

m=Motorcycle('black',2,10)
print(m.Color)
m.Put_Helmet()
m.Move()
m.Park()


c=Car('gray',2,10)
print(c.Color)
c.Turn_on_Radio()
c.Move()
c.Park()
