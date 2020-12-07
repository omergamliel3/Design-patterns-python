# Decorator pattern

class Interface:
    def description(self):
        raise NotImplementedError
    def cost(self):
        raise NotImplementedError

class Concrete(Interface):
    def description(self):
        pass
    def cost(self):
        pass


def main():
    pass

if __name__ == "__main__":
    main()