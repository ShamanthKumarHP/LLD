# crux: Providing a wrapper as a layer of abstraction

# can also have facade for further delegated operations

class CPU:
    def start(self):
        print("Starting CPU")

class RAM:
    def clean(self):
        print("Starting RAM")

class IO:
    def initialize(self):
        print("Starting IO")

class ComputerSystemFacade:
    def __init__(self):
        self.cpu = CPU()
        self.ram = RAM()
        self.io = IO()
    
    def startComputer(self):
        self.cpu.start()
        self.ram.clean()
        self.io.initialize()
    

if __name__ == "__main__":
    computer = ComputerSystemFacade()
    computer.startComputer()

        