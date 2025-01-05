from FurnitureFactory import FurnitureFactory, ModernFurnitureFactory, TraditionalFurnitureFactory, VintageFurnitureFactory

def get_furniture_details(factory: FurnitureFactory):
    
    sofa = factory.create_sofa()
    table = factory.create_table()

    sofa.display_details()
    table.display_details()

def main():
    modern_factory = ModernFurnitureFactory()
    get_furniture_details(modern_factory)

if __name__ == "__main__":
    main()