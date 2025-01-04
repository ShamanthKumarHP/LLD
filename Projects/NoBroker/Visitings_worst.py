class Visitor:
    def __init__(self, name):
        self.name = name
        self.visits = []

    def add_visit(self, visit):
        self.visits.append(visit)

    def __str__(self):
        return f"Visitor {self.name}"


class Visit:
    def __init__(self, address, price):
        self.address = address
        self.price = price
        self.visitors = []

    def add_visitor(self, visitor):
        self.visitors.append(visitor)

    def __str__(self):
        return f"Visit to {self.address} costing {self.price}"


# Example usage
visitor1 = Visitor("John")
visitor2 = Visitor("Alice")
visit1 = Visit("123 Main St", 500000)

visitor1.add_visit(visit1)
visitor2.add_visit(visit1)

visit1.add_visitor(visitor1)
visit1.add_visitor(visitor2)


# Bi-directional Relationship:

# The code maintains a bi-directional relationship between Visitor and Visit. 
# This means that if you have a Visit, you can access the visitors, and if you have a Visitor, you can access the visits. This can be useful depending on the use case.

# Cons of the Design:
# 1. Tight Coupling Between Visitor and Visit: any change in one class might require changes in the other
# 2. Potential for Data Inconsistencies: Hard to maintain two lists in sync
# 3. Violates SRP: As one class is managing another class.
# 4. Flexibility:
"""
How to handle scenarios where visitors cancel a visit or visits are deleted?
The current design might require significant changes in both Visitor and Visit classes, leading to fragile design.
"""