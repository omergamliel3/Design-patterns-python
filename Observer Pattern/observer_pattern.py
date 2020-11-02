# Observer pattern

# Observer Interface
class ObserverInterface:
    def update(self):
        raise NotImplementedError

# Observable Interface
class ObservableInterface:
    def add(self,  observer: ObserverInterface):
        raise NotImplementedError

    def remove(self, observer: ObserverInterface):
        raise NotImplementedError

    def notify(self):
        raise NotImplementedError

# Implement concrete observable
class ConcreteObservable(ObservableInterface):
    def __init__(self):
        # maintains all observers
        self.observers = []
        # set state to Initial
        self.state = 'Initial'

    # add observer to observers list
    def add(self, observer: ObserverInterface):
        self.observers.append(observer)

    # remove observer to observers list
    def remove(self, observer: ObserverInterface):
        self.observers.remove(observer)

    # notify all observers
    def notify(self):
        for observer in self.observers:
            observer.update()

    # return the current state
    def getState(self):
        return self.state
    
    # assign new state and notify observers
    def emit(self, state: str):
        self.state = state
        self.notify()


# Implement concrete observer 
class ConcreteObserver(ObserverInterface):
    def __init__(self, observable: ConcreteObservable):
        self.subject = observable

    def update(self):
        state = self.subject.getState()
        print(f'Update Concrete Observer\nState: {state}')

# main 
def main():
    # create observable instance
    observable = ConcreteObservable()
    # create observer A instance
    observerA = ConcreteObserver(observable)
    # create observer B instance
    observerB = ConcreteObserver(observable)
    # add observer A to observable 
    observable.add(observerA)
    # add observer B to observable 
    observable.add(observerB)
    # emits new state
    observable.emit('Initial')
    # emits new state
    observable.emit('Loading')
    # emits new state
    observable.emit('Error')
    # emits new state
    observable.emit('Data')


if __name__ == "__main__":
    main()