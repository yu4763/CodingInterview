class Animal:
    order = None
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def order(self, order):
        self.order = order


class Dog(Animal):
    def order(self, order):
        self.order = order


class Queue:
    def __init__(self):
        self.cat = []
        self.dog = []
        self.cnt = 0

    def enqueue(self, pet):
        pet.order(self.cnt)
        self.cnt += 1
        if isinstance(pet, Cat):
            self.cat.append(pet)
        else:
            self.dog.append(pet)

    def dequeueAny(self):
        if self.isEmpty():
            print("empty")
            return
        elif len(self.cat) == 0:
            pet = self.dog.pop(0)
            return pet

        elif len(self.dog) == 0:
            pet = self.cat.pop(0)
            return pet

        c = self.cat[0]
        d = self.dog[0]
        if c.order < d.order:
            pet = self.cat.pop(0)
            return pet
        else:
            pet = self.dog.pop(0)
            return pet

    def dequeueCat(self):
        pet = self.cat.pop(0)
        return pet

    def dequeueDog(self):
        pet = self.dog.pop(0)
        return pet

    def isEmpty(self):
        if len(self.cat) == 0 and len(self.dog)== 0:
            return True
        else:
            return False



if __name__ == "__main__":
    pets = Queue()
    pets.enqueue(Cat("a"))
    pets.enqueue(Cat("b"))
    pets.enqueue(Dog("A"))
    pets.enqueue(Cat("c"))
    pets.enqueue(Dog("B"))
    pets.enqueue(Dog("C"))
    pets.enqueue(Dog("D"))
    pets.enqueue(Cat("d"))

    for i in range(3):
        pet = pets.dequeueDog()
        print(pet.name)

    # while not pets.isEmpty():
    #     pet = pets.dequeueAny()
    #     print(pet.name)
