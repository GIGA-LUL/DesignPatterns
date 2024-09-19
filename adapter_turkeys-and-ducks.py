class Duck:
    def quack(self):
        pass

    def fly(self):
        pass


class MallardDuck(Duck):
    def quack(self):
        print("Quack")

    def fly(self):
        print("I’m flying")


class Turkey:
    def gobble(self):
        pass

    def fly(self):
        pass


class WildTurkey(Turkey):
    def gobble(self):
        print("Gobble gobble")

    def fly(self):
        print("I’m flying a short distance")


class TurkeyAdapter(Duck):
    def __init__(self, turkey_object):
        self.turkey = turkey_object

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for _ in range(5):
            self.turkey.fly()


def test_duck(duck_object):
    duck_object.quack()
    duck_object.fly()


if __name__ == "__main__":
    duck = MallardDuck()
    turkey = WildTurkey()
    turkey_adapter = TurkeyAdapter(turkey)

    print("The Turkey says...")
    turkey.gobble()
    turkey.fly()

    print("\nThe Duck says...")
    test_duck(duck)

    print("\nThe TurkeyAdapter says...")
    test_duck(turkey_adapter)
