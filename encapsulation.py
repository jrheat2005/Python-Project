class Protected:
    def __init__(self):
        # Private attribute
        self.__private_var = 42

        # Protected attribute
        self._protected_var = "Hello, protected!"

    def use_encapsulation(self):
        # Accessing private attribute
        private_value = self.__private_var
        print("Private attribute:", private_value)

        # Accessing protected attribute
        protected_value = self._protected_var
        print("Protected attribute:", protected_value)


# Creating an object of the class
obj = Protected()

# Using encapsulated attributes
obj.use_encapsulation()



