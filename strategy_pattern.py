# Strategy pattern 

# Behavior Interface
class BehaviorInterface():
    def run(self):
        raise NotImplementedError

# Concrete BehaviorInterface
class ConcreteBehaviorA(BehaviorInterface):
    def run(self):
        print('run concrete behavior A')


# Concrete BehaviorInterface
class ConcreteBehaviorB(BehaviorInterface):
    def run(self):
        print('run concrete behavior B')

# Client
class Client():
    # inject BehaviorInterface type with constructor
    def __init__(self, behavior: BehaviorInterface):
        self.behavior = behavior

    # evoke behavior run()
    def execute(self):
        self.behavior.run()


# main
def main():
    # create behaviors
    behaviorA = ConcreteBehaviorA()
    behaviorB = ConcreteBehaviorB()
    # create client and inject behaviors
    clinetA = Client(behaviorA)
    clientB = Client(behaviorB)
    # evoke execute
    clinetA.execute()
    clientB.execute()


if __name__ == "__main__":
    main()
