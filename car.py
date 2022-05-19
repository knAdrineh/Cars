# Adrineh Khodaverdian
# CS/IS 151
# cars labs

# cars simulation class

class Car:
    MAXIMUM_SPEED = 120

    # the default constructor
    def __init__(self):
        self.__make = ""
        self.__model = ""
        self.__year = ""
        self.__speed = 0

    # the 4 argument constructor
    def __init__(self, make, model, year, speed):
        self.__make = make
        self.__model = model
        self.__year = year
        if speed >= 0:
            self.__speed = speed
        else:
            self.__speed = 0

    ###########################
    #      Set methods        #
    ###########################
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def set_speed(self, speed):
        self.__speed = speed

    ###########################
    #      get methods        #
    ###########################
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_speed(self):
        return self.__speed

    # string convertor
    def __str__(self):
        return f'Car, make: {self.__make}, model: {self.__model}, year: {self.__year}, speed: {self.__speed}'

    # additional functions
    def accelerate(self, speed):
        if speed < 0 or speed > 20:
            print("Invalid acceleration value: {}".format(speed))
        elif self.__speed + speed >= 120:
            print("This car has reached its maximum speed: 120")
            self.__speed = 120
        else:
            self.__speed += speed

    def brake(self, speed):
        if speed < 0 or speed > 20:
            print("Invalid braking value: {}".format(speed))
        elif self.__speed - speed == 0 or self.__speed - speed < 0:
            print("This car has stopped")
            self.__speed = 0
        else:
            self.__speed -= speed
