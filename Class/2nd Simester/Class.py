class animal:
    def speak(self):
        print("Animal Speaking")
class Dog(animal):
    def bark(self):
        print("Dog Barking")

obj = Dog()
obj.bark()
obj.speak()