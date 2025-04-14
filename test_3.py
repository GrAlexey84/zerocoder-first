class Bird():
    def fly(self):
        print("Птица летает")

class Duck(Bird):
    def fly(self):
        print("Утка летит низко")


def fly_in_the_sky(animal):
    animal.fly()

b = Bird()
d = Duck()

fly_in_the_sky(b)
fly_in_the_sky(d)