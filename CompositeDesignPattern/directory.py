# crux: Allowing a single object or composite of objects to be treated uniformly
# For example: File or Directory both will have size, Last Modified, etc properities
# Here Directory is a list of Files

# has a + is a

from abc import ABC, abstractmethod

# Abstraction Layer
class File_system(ABC):

    @abstractmethod
    def getSize(self):
        pass

    @abstractmethod
    def displayContents(self):
        pass


# refined concrete class
class Files(File_system):

    def __init__(self, fname, size):
        self.name = fname
        self.size = size
    
    def getSize(self):
        return self.size

    def displayContents(self):
        print(f"File Name: {self.name}")


# refined concrete class
class Directory(File_system):
    # has a + is a
    def __init__(self, dname):
        self.name = dname
        self.fs_list = [] # list to store type FileSystem; 
    
    def displayContents(self):
        print("Directory name", self.name)
        for fs in self.fs_list:
            fs.displayContents()
    
    def getSize(self):
        total_size = 0
        for fs in self.fs_list:
            total_size += fs.getSize()
        return total_size
    
    def addComponents(self, fs):
        self.fs_list.append(fs) # it could be file or directory


if __name__ == "__main__":
    file1 = Files("file1.py", 10)
    file2 = Files("file2.txt", 20)

    dir1 = Directory("/tmp")    
    dir1.addComponents(file1)

    dir2 = Directory("/root")
    dir2.addComponents(file2)
    dir2.addComponents(dir1)

    print("Dir1 contents")
    dir1.displayContents()
    print()
    print("Dir2 contents")
    dir2.displayContents()
    print()
    print("Dir2 size", dir2.getSize())


