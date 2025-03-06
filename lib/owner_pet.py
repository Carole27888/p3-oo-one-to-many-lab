
class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # Class variable to store all pet instances
    
    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type!")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)  # Add the pet instance to the all list
        if owner:
            owner.add_pet(self)  # Assign pet to the owner if an owner is passed

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # Initialize an empty list of pets for each owner
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Can only add instances of Pet")
        pet.owner = self  # Set the pet's owner to this instance
        self._pets.append(pet)  # Add the pet to this owner's pet list
    
    def pets(self):
        return self._pets  # Return the list of pets owned by this owner
    
    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)  # Return pets sorted by name
