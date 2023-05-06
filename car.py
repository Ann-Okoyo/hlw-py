class Car:
    wheels=4
    def __init__(self,make,model,color):
        self.make=make
        self.model=model
        self.color=color
    def hooting(self):
        return "peep peep"
    def accelerate(self,kmh):
        self.speed+=kmh
        return f"Accelerating to {self.speed} kmh"
        
    def car_stop(self):
        self.speed=0
        return"The car is stopping"
    
    car1=Car("Porsche","Mercedez","Range rover")
    car2=Car("Volvo","Subaru","BMW")


    print(car1.hooting())
    print(car1.accelerate(30))
    print(car1.car_stop())

    car2.accelerate(80)
    car2.car_stop()
    