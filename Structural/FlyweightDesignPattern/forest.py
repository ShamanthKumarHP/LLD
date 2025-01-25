# crux: When we have multiple objects that has same attributes(Intrinsic state)

# Flyweight class : has intrinsic state shared across many tree
class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture
    
    def plant(self, x, y):
        print("Placed Tree at", x, y)


# TreeFactory is responsible for creating and managing TreeType objects
"""
@classmethod is useful when you need to modify or operate on class-level variables
class TreeFactory:
    tree_types = {}

    @classmethod
    def get_tree_type(cls, name, color, texture) -> TreeType:
        t_type = f"{name}-{color}-{texture}"
        if t_type not in cls.tree_types:
            cls.tree_types[t_type] = TreeType(name, color, texture)
        return cls.tree_types[t_type]

"""

# static method is preferred as we are not managing the state of class unlike singleton
class TreeFactory:
    tree_types = {}

    @staticmethod
    def get_tree_type(name, color, texture) -> TreeType:
        t_type = f"{name}-{color}-{texture}"
        if t_type not in TreeFactory.tree_types:
            TreeFactory.tree_types[t_type] = TreeType(name, color, texture)
        return TreeFactory.tree_types[t_type]


class Tree:
    def __init__(self, x, y, tree_type : TreeType):
        self.x = x
        self.y = y
        self.tree_type = tree_type
    
    def plant(self):
        # Note: we are not writing definition here, bcoz flyweight class has to do implementation. 
        # we are having centric implementation.
        # coz: we dont want to access intrinsic params in each object. also causes storage overhead
        self.tree_type.plant(self.x, self.y)


class Forest:
    def __init__(self):
        self.trees = []
    
    def create_tree(self, name, color, texture, x, y):
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)
        return tree
    
    def plant_tress(self):
        for tree in self.trees:
            tree.plant()
    

class Demo:
    forest = Forest()
    tree1 = forest.create_tree("Oak", "green", "rough", 10, 20)
    tree2 = forest.create_tree("Teek", "green", "smooth", 20, 30)
    
    
    tree3 = forest.create_tree("Oak", "green", "rough", 100, 200)
    tree4 = forest.create_tree("Teel", "green", "smooth", 200, 300)

    forest.plant_tress()




