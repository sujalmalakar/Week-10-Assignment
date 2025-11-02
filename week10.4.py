import random


class Car:
    def __init__(self, reg_num, max_speed, current_speed=0, travelled_distance=0):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, number_of_hours):
        self.travelled_distance += number_of_hours * self.current_speed


class Race:
    def __init__(self, name, distance, car_list):
        self.name = name
        self.distance = distance
        self.car_list = car_list

    def hour_passes(self):
        for car in self.car_list:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"| {'Reg. Num':<10} | {'Max Speed (km/h)':<16} | {'Current Speed (km/h)':<20} | {'Distance (km)':<15} |")
        print("-" * 71)
        sorted_cars = sorted(self.car_list, key=lambda c: c.travelled_distance, reverse=True)
        for car in sorted_cars:
            print(
                f"| {car.reg_num:<10} | {car.max_speed:<16} | {car.current_speed:<20} | {car.travelled_distance:<15.0f} |")

    def race_finished(self):
        for car in self.car_list:
            if car.travelled_distance >= self.distance:
                return True
        return False


if __name__ == "__main__":

    cars = []
    for i in range(1, 11):
        reg_num = f"ABC-{i}"
        max_s = random.randint(100, 200)
        cars.append(Car(reg_num, max_s))

    grand_derby = Race(name="Grand Demolition Derby", distance=8000, car_list=cars)

    hours_elapsed = 0

    print(f"Starting Race: {grand_derby.name} ({grand_derby.distance} km)")

    while not grand_derby.race_finished():
        grand_derby.hour_passes()
        hours_elapsed += 1

        if hours_elapsed % 10 == 0:
            grand_derby.print_status()

    print(f"\nRace Finished in {hours_elapsed} hours!")
    print("Final Standings")
    grand_derby.print_status()