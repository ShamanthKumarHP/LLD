from abc import ABC, abstractmethod


# State Interface (Abstract Class)
class State(ABC):
    @abstractmethod
    def pressPowerButton(self, phone):
        pass
    
    def pressHomeButton(self, phone):
        pass

# Concrete States

class LockedState(State):
    def pressPowerButton(self, phone):
        print("Phone is locked. enter password")
        phone.setState(UnlockedState())  # After pressing a button, the phone will unlock.

    def pressHomeButton(self, phone):
        print("Do nothing")


class UnlockedState(State):
    def pressPowerButton(self, phone):
        print("Phone is getting locked.")
        phone.setState(LockedState())
    
    def pressHomeButton(self, phone):
        print("Phone is in Home page")


class LockedOnDisplay(State):
    def pressPowerButton(self, phone):
        print("Turning off screen")
        phone.setState(LockedState())
    
    def pressHomeButton(self, phone):
        print("Do nothing")


# Phone (Context) Class
class Phone:
    def __init__(self):
        self._state = LockedState()
    
    def setState(self, state: State):
        self._state = state
    
    def pressHomeButton(self):
        # Delegate button press to the current state
        self._state.pressHomeButton(self)
    
    def pressPowerButton(self):
        self._state.pressPowerButton(self)


# Client code to simulate the behavior
if __name__ == "__main__":
    # Initial state is LockedState
    phone = Phone()
    
    print("Initial state: Locked")
    phone.pressPowerButton()  
    
    print("\nState changed to Unlocked")
    phone.pressPowerButton()  
    

    print("\nState changed to Locked")
    phone.setState(LockedState())
    phone.pressHomeButton()  
