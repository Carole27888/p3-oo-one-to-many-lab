# owner_pet.py

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # Class variable to keep track of all pet instances

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        # Validate pet_type
        if self.pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {self.pet_type}. Must be one of {Pet.PET_TYPES}")

        # Add this pet to the all list
        Pet.all.append(self)

    def __str__(self):
        return f"{self.name} the {self.pet_type}"

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # List to store the owner's pets

    def pets(self):
        """Returns a list of the owner's pets."""
        return self._pets

    def add_pet(self, pet):
        """Adds a pet to the owner's list of pets if it's a valid Pet instance."""
        if not isinstance(pet, Pet):
            raise Exception("The object is not a valid Pet instance.")
        pet.owner = self  # Set the owner of the pet
        self._pets.append(pet)  # Add the pet to the owner's list of pets

    def get_sorted_pets(self):
        """Returns a sorted list of the owner's pets by their name."""
        return sorted(self._pets, key=lambda pet: pet.name)

    def __str__(self):
        return f"Owner: {self.name}"
