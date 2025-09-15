class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_info(self):
        print(self.name)
        print(self.age)
    def age_years(self, years):
        for i in range(years):
            self.age += 1
            print("Happy birthday! " + self.name + " is turning " + str(self.age) + " years old this year!")
    def born(self):
        print(self.name + " was born")
        self.age = 0
    def die(self):
        print(self.name + " died")
        print("f")


class Dog:
    def __init__(self, name):
        self.name = name
    def play(self):
        print(self.name + " is playing")
    def sleep(self):
        print(self.name + " is sleeping")
    def day_cycle(self):
        self.sleep()
        self.play()
        self.play()
        self.sleep()
        self.play()
        self.play()
        self.sleep()

class Puppy(Dog):
    def day_cycle(self):
        for i in range(5):
            self.sleep()
        self.play()
        self.sleep() #lazy