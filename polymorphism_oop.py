class Parrot:

    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can`t swim")

class Penguin:

    def fly(self):
        print("Penguin can`t fly")

    def swim(self):
        print("Penguin can Swim")

# common interface
def flying_test(bird):
    bird.fly()

def swimming_test(bird):
    bird.swim()

# instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)


swimming_test(blu)
swimming_test(peggy)
