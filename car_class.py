class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
        
    def accelerate(self):
        self.__speed += 5
    def brake(self):
        self.__speed -= 5
    def get_speed(self):
        return self.__speed
        
def test_car():
    car = Car(2024, "Toyota")
    
    for _ in range(5):
        car.accelerate()
        print("Speed after accelerating:", car.get_speed())
    for _ in range(5):
        car.brake()
        print("Speed after braking:", car.get_speed())

test_car()