# To create similar copies of an object.
# Just will have a wrapper for copy

from abc import ABC, abstractmethod

class Button_Prototype(ABC):
    @abstractmethod
    def clone():
        pass

    @abstractmethod
    def display():
        pass

    # just if we want to update anything during clone
    @abstractmethod
    def update_text():
        pass

class Menu_Botton(Button_Prototype):
    def __init__(self, text=None, height=None, width=None):
        self.text = text
        self.height = height
        self.width = width
    
    def clone(self):
        return Menu_Botton(self.text, self.height, self.width)
    
    def display(self):
        print(f"text = {self.text}")
        print(f"height = {self.height}")
        print(f"width = {self.width}")
    
    def update_text(self, text):
        self.text = text

if __name__ == '__main__':
    button1 = Menu_Botton(text="welcome", height="10px", width="30px")
    button2 = button1.clone()
    button2.display()
    button2.update_text("thanks")
    button2.display()
    button1.display()



            

    

        
