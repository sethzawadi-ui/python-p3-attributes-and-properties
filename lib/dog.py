class Dog:
    APPROVED_BREEDS = ["Husky", "Golden Retriever", "Pug", "Dalmatian", "Mutt"]

    def __init__(self, name=None, breed="Mutt"):
        # Validate breed FIRST (because tests call Dog(breed="...") with no name)
        if breed not in Dog.APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
            return

        # Name is optional — validate only if provided
        if name is not None:
            if not isinstance(name, str) or len(name) == 0 or len(name) > 25:
                print("Name must be string between 1 and 25 characters.")
                return

        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")
