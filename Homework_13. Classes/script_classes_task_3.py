class Car:
    def __init__(self, brand, model, year, speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        self.speed += 5
        return self.speed

    def brake(self):
        self.speed -= 5

        if self.speed < 0:
            self.speed = 0

        else:
            return self.speed
        
    def display_speed(self):
        return self.speed