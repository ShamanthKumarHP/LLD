class Visitor:
    def __init__(self, visitorID, name):
        self.visitorID = visitorID  # Unique identifier for the visitor
        self.name = name
        self.visitIDs = []  # List to store all visitIDs

    def attend_visit(self, visit):
        """Assign a visit to this visitor by storing the visitID."""
        if visit.visitID not in self.visitIDs:  # Avoid duplicates
            self.visitIDs.append(visit.visitID)

    def __str__(self):
        return f"Visitor {self.name} (ID: {self.visitorID})"


class Visit:
    def __init__(self, visitID, address, price):
        self.visitID = visitID  # Unique identifier for this visit
        self.address = address
        self.price = price
        self.visitorIDs = []  # A list of VisitorIDs who attended this visit

    def add_visitor(self, visitor):
        """Add a visitor to this visit."""
        if visitor.visitorID not in self.visitorIDs:
            self.visitorIDs.append(visitor.visitorID)
            visitor.attend_visit(self)  # Add the visitID to the visitor's list
        else:
            print(f"{visitor.name} is already registered for this visit.")

    def __str__(self):
        return f"Visit to {self.address} costing {self.price}"


class VisitManager:
    def __init__(self):
        self.visits = {}  # Store visits in a dictionary where key is visitID
        self.visitors = {}  # Store visitors in a dictionary where key is visitorID

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

    def get_visit_by_id(self, visitID):
        """Return a visit by its ID."""
        return self.visits.get(visitID, None)

    def get_visitor_by_id(self, visitorID):
        """Return a visitor by their ID."""
        return self.visitors.get(visitorID, None)

    def get_visits_for_visitor(self, visitor):
        """Return the visit(s) attended by a specific visitor."""
        visited_visits = [self.get_visit_by_id(visitID) for visitID in visitor.visitIDs if self.get_visit_by_id(visitID)]
        return visited_visits

    def get_visitors_for_visit(self, visit):
        """Return the visitors for a specific visit."""
        return [self.get_visitor_by_id(visitorID) for visitorID in visit.visitorIDs if self.get_visitor_by_id(visitorID)]


# Example usage
visitor1 = Visitor(1, "John")
visitor2 = Visitor(2, "Alice")
visit1 = Visit(1, "123 Main St", 500000)
visit2 = Visit(2, "456 Elm St", 300000)
visit3 = Visit(3, "789 Oak St", 450000)

manager = VisitManager()
manager.register_visit(visit1)
manager.register_visit(visit2)
manager.register_visit(visit3)
manager.register_visitor(visitor1)
manager.register_visitor(visitor2)

# Adding visitors to visits
visit1.add_visitor(visitor1)
visit1.add_visitor(visitor2)
visit2.add_visitor(visitor1)  # John attends visit2 as well
visit3.add_visitor(visitor2)  # Alice attends visit3

# Print visitors for a visit
print(f"Visitors for {visit1.address}:")
for v in manager.get_visitors_for_visit(visit1):
    print(v)

# Print visits for a visitor
print(f"\nVisits for {visitor1.name}:")
for v in manager.get_visits_for_visitor(visitor1):
    print(v)

# Still there is indirect dependency of IDs. Classes stores references to the other class.

# Point is to have SRP
# Have the VisitManager or some other external service 
# to take full responsibility for maintaining the relationships 
# between Visitor and Visit objects.