class Oven:

    def __init__(self, brand, model, capacity):

        self.brand = brand

        self.model = model

        self.capacity = capacity

        self.temperature = 0

        self.timer = 0

        self.is_powered_on = False



    def power_on(self):

        if not self.is_powered_on:

            self.is_powered_on = True

            print(f"{self.brand} {self.model} is now powered on.")

        else:

            print("The oven is already powered on.")



    def power_off(self):

        if self.is_powered_on:

            self.is_powered_on = False

            self.temperature = 0

            self.timer = 0

            print(f"{self.brand} {self.model} is now powered off.")

        else:

            print("The oven is already powered off.")



    def set_temperature(self, temperature):

        if self.is_powered_on:

            self.temperature = temperature

            print(f"Temperature set to {temperature} degrees Celsius.")

        else:

            print("Please power on the oven first.")



    def set_timer(self, minutes):

        if self.is_powered_on:

            self.timer = minutes

            print(f"Timer set for {minutes} minutes.")

        else:

            print("Please power on the oven first.")



    def start_cooking(self):

        if self.is_powered_on:

            if self.temperature > 0 and self.timer > 0:

                print("Cooking started.")

            else:

                print("Please set temperature and timer before starting to cook.")

        else:

            print("Please power on the oven first.")



    def __str__(self):

        return f"{self.brand} {self.model}, Capacity: {self.capacity}L"

