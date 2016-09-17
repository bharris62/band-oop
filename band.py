# In python, an instance is, for example, a specific musician in a music class.


class Musician(object):
    def __init__(self, sounds): # method, as in, a function in a class
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=' ')
        print()


class Bassist(Musician):  # The Musician Class is the parent class
    def __init__(self):
        # call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])


class Guitarist(Musician):
    def __init__(self):
        super().__init__(["Boing", "Bow", "Boom"])


    def tune(self):
        print("Be with you in a moment")
        print("Twoning, Sproing, Splang")


class Drummer(Musician):
    def __init__(self):
        super().__init__(['Boom', "Boom", "Cha", "Boom"])

    def count_in(self):
        print("1 and 2 and 3 and 4")

    def combust(self):
        print("aaarrrggghhh BOOM")

class Band(Musician):

    def __init__(self):
        print("created, band")

    def fire(self):
        print("You're fired!")

    def hire(self):
        print("You're hired!")


def main():
    John = Guitarist()
    John.solo(6)

    Adam = Drummer()
    Adam.count_in()
    Adam.combust()

    Blink = Band()
    Blink.fire()


if __name__ == '__main__':
    main()

