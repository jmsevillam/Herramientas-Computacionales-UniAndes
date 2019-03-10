class Dog:
    def __init__(self,name,posx,posy):
        self.name=name
        self.posx=posx
        self.posy=posy
        self.awaken=False
        self.hungry=False
        self.counter=0
    def awake(self):
        if self.awaken:
            print(self.name+' is already awaken')
        else:
            self.awaken=True
            print(self.name+' is no longer slept')
    def move(self,x1,y1):
        if self.hungry:
            print(self.name+' is hungry')
        elif self.awaken:
            self.posx+=x1
            self.posy+=y1
            self.counter+=1
        else:
            print(self.name+' is slept')
        if self.counter>=3:
            self.hungry=True
    def feed(self):
        self.counter=0
        self.hungry=False
        print(self.name+' is no longer hungry')

MyDog=Dog('Lambda',0,0)
print(MyDog.posx,MyDog.posy)
MyDog.move(1,1)
MyDog.awake()
MyDog.move(1,0)
print(MyDog.posx,MyDog.posy)
MyDog.move(0,1)
print(MyDog.posx,MyDog.posy)
MyDog.move(1,1)
print(MyDog.posx,MyDog.posy)
MyDog.move(1,1)
print(MyDog.posx,MyDog.posy)
MyDog.feed()
MyDog.move(1,0)
print(MyDog.posx,MyDog.posy)
