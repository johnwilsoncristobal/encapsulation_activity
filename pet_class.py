class Pet:
    def __init__(self, name="", animal_type="", age=0):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
        
    # Setters
    def set_name(self, name):
        self.__name = name
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    def set_age(self, age):
        self.__age = age

    # Getters
    def get_name(self):
        return self.__name
    def get_animal_type(self):
        return self.__animal_type
    def get_age(self):
        return self.__age
        
def test_pet():
    pet = Pet()
    pet.set_name(input("Enter pet name: "))
    pet.set_animal_type(input("Enter pet type: "))
    pet.set_age(int(input("Enter pet age: ")))
    print("Pet Details: Name:", pet.get_name(),"Type:", pet.get_animal_type(),"Age:", pet.get_age())

test_pet()