#Adrineh Khodaverdian
#CS/IS 151
import sys

from car import Car

def main():
    found = False
    cars = list()
    col = list()
    speed = 0
    counter = 0
    while not found:
        try:
            csv_file = open(sys.argv[1])
            # Read the file's lines into
            lines = csv_file.readlines()
            # Close the file.
            csv_file.close()
            #process the lines
            for line in lines:
                tokens = line.split(',')
                car = Car(tokens[0], tokens[1], tokens[2], 0) #the first three columns are the make, model and year
                for cols in range(3,len(tokens)):
                    if int(tokens[cols]) >= 0:
                        car.accelerate(int(tokens[cols]))
                    else:
                        car.brake(abs(int(tokens[cols])))
                cars.append(car) #adds car to the cars list
                
            cars = sorted(cars, key=lambda car: car.get_speed(), reverse=True)
            print("Winner: {}".format(cars[0]))
            print("Runner up: {}".format(cars[1]))
            print("3rd finisher: {}".format(cars[2]))

            #now the file is read and printed and found so done
            found = True
        except FileNotFoundError:
            print("File {} does not exist in the directory")



main()
