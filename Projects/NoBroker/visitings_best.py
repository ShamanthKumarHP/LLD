class Visitor:
    def __init__(self, visitorID, name):
        self.visitorID = visitorID  # Unique identifier for the visitor
        self.name = name
        # Removed visitIDs from here

    def __str__(self):
        return f"Visitor {self.name} (ID: {self.visitorID})"


class Visit:
    def __init__(self, visitID, address, price):
        self.visitID = visitID  # Unique identifier for this visit
        self.address = address
        self.price = price
        # Removed visitorIDs from here

    def __str__(self):
        return f"Visit to {self.address} costing {self.price}"


class VisitManager:
    def __init__(self):
        self.visits = {}  # Store visits by visitID
        self.visitors = {}  # Store visitors by visitorID
        self.visitor_visit_map = {}  # Maps visitorID to a list of visitIDs
        self.visit_visitor_map = {}  # Maps visitID to a list of visitorIDs

    def register_visit(self, visit):
        """Register a new visit using the visitID as the key."""
        if visit.visitID not in self.visits:
            self.visits[visit.visitID] = visit
        else:
            print(f"Visit with ID {visit.visitID} is already registered.")

    def register_visitor(self, visitor):
        """Register a new visitor using the visitorID as the key."""
        if visitor.visitorID not in self.visitors:
            self.visitors[visitor.visitorID] = visitor
        else:
            print(f"Visitor with ID {visitor.visitorID} is already registered.")

    def add_visitor_to_visit(self, visitor, visit):
        """Link a visitor to a visit."""
        # Add visitID to visitor's visit list in the mapping
        if visitor.visitorID not in self.visitor_visit_map:
            self.visitor_visit_map[visitor.visitorID] = []
        self.visitor_visit_map[visitor.visitorID].append(visit.visitID)
        
        # Add visitorID to visit's visitor list in the mapping
        if visit.visitID not in self.visit_visitor_map:
            self.visit_visitor_map[visit.visitID] = []
        self.visit_visitor_map[visit.visitID].append(visitor.visitorID)

    def get_visits_for_visitor(self, visitor):
        """Return the visits attended by a specific visitor."""
        visitIDs = self.visitor_visit_map.get(visitor.visitorID, [])
        return [self.visits[visitID] for visitID in visitIDs]

    def get_visitors_for_visit(self, visit):
        """Return the visitors for a specific visit."""
        visitorIDs = self.visit_visitor_map.get(visit.visitID, [])
        return [self.visitors[visitorID] for visitorID in visitorIDs]


# Example usage
visitor1 = Visitor(1, "John")
visitor2 = Visitor(2, "Alice")
visit1 = Visit(1, "123 Main St", 500000)
visit2 = Visit(2, "456 Elm St", 300000)

manager = VisitManager()
manager.register_visit(visit1)
manager.register_visit(visit2)
manager.register_visitor(visitor1)
manager.register_visitor(visitor2)

# Adding visitors to visits
manager.add_visitor_to_visit(visitor1, visit1)
manager.add_visitor_to_visit(visitor2, visit1)
manager.add_visitor_to_visit(visitor1, visit2)

# Get visits for a visitor
print(f"Visits for {visitor1.name}:")
for visit in manager.get_visits_for_visitor(visitor1):
    print(visit)

# Get visitors for a visit
print(f"\nVisitors for {visit1.address}:")
for visitor in manager.get_visitors_for_visit(visit1):
    print(visitor)


# Association is the correct term for the relationship when VisitManager holds only a visitID and not the full Visit object.
# VisitManager holds only the visitID (a form of reference) and does not create or own Visit objects, this relationship could also be described as aggregation.
# The distinction between aggregation and association in this case is subtle and can often overlap


# why to have dedicated class for creation/ scheduling/ deletion of visits?
# Cohesion: methods and properties should be highly related to each other in a class
# If the VisitManager is dealing with scheduling, creation, and deletion, it may become too "bloated" with responsibilities.
# so have dedicated classes to maintain SRP too

class VisitScheduler:
    def __init__(self, visit_manager):
        self.visit_manager = visit_manager

    def schedule_visit(self, address, price):
        visitID = self._generate_visitID()  # A method to generate unique visitIDs
        new_visit = Visit(visitID, address, price)
        self.visit_manager.register_visit(new_visit)
        return new_visit

    def _generate_visitID(self):
        # Some logic to generate a unique visitID
        return len(self.visit_manager.visits) + 1


class VisitDeleter:
    def __init__(self, visit_manager):
        self.visit_manager = visit_manager

    def delete_visit(self, visitID):
        if visitID in self.visit_manager.visits:
            del self.visit_manager.visits[visitID]
            print(f"Visit {visitID} has been deleted.")
        else:
            print(f"Visit {visitID} not found.")