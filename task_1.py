class Animal:
    def __init__(self):
        pass

    def talk(self):
        raise NotImplementedError("Має бути підкласом")

    def print_talk(self, speech):
        self.speech = speech
        return print(speech)


class Cat(Animal):
    def talk(self):
        print("Мяу")


class Dog(Animal):
    def talk(self):
        print("Гав!")


my_cat = Cat()
my_cat.talk()
my_cat.print_talk("Мяу-мяу")
