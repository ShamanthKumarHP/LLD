# We will have a Command Interface, Concrete Commands, 
# May have abstract Receiver, and Concrete Receiver
# Invoker

from abc import ABC, abstractmethod

# Abstract reciever Command
class Document:
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def save(self):
        pass

# Concrete reciever commands
class WordDocument(Document):
    def open(self):
        print("Opening word document")
        return
    
    def save(self):
        print("Saving Word document")

class GoogleDocument(Document):
    def open(self):
        print("Opening Google Document")
    
    def save(self):
        print("Saving google document")

# Abstract Command
class ActionCommand:
    @abstractmethod
    def execute(self):
        pass

# Concrete Commands
class ActionCommandSave:
    def __init__(self, doc_type):
        self.doc = doc_type
        
    def execute(self):
        self.doc.save()
    
class ActionCommandOpen:
    def __init__(self, doc_type):
        self.doc = doc_type
    
    def execute(self):
        self.doc.open()

# Invoker
class MenuOptions:
    def __init__(self):
        self.commands_list = [] # type :ActionCommand # we can use it for undo/redo also 
    
    def addCommand(self, cmd):
        self.commands_list.append(cmd)
    
    def executeCommand(self):
        for cmd in self.commands_list:
            cmd.execute()

# Client
if __name__ == "__main__":
    doc_type = GoogleDocument()

    menu_options = MenuOptions()

    menu_options.addCommand(ActionCommandOpen(doc_type))
    menu_options.addCommand(ActionCommandSave(doc_type))

    menu_options.executeCommand()


    



