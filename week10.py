class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Floor: {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Floor: {self.current_floor}")

    def go_to_floor(self, target_floor):
        if target_floor > self.top_floor:
            target_floor = self.top_floor
        elif target_floor < self.bottom_floor:
            target_floor = self.bottom_floor

        if target_floor > self.current_floor:
            print(f"--- Going UP from {self.current_floor} to {target_floor} ---")
            while self.current_floor < target_floor:
                self.floor_up()

        elif target_floor < self.current_floor:
            print(f"--- Going DOWN from {self.current_floor} to {target_floor} ---")
            while self.current_floor > target_floor:
                self.floor_down()

        print(f"--- Arrived at floor {self.current_floor} ---")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for i in range(num_elevators):
            e = Elevator(bottom_floor, top_floor)
            self.elevators.append(e)
            print(f"Elevator {i} created.")

    def run_elevator(self, elevator_num, target_floor):
        if 0 <= elevator_num < len(self.elevators):
            print(f"\n*** Running Elevator {elevator_num} ***")
            elevator = self.elevators[elevator_num]
            elevator.go_to_floor(target_floor)
        else:
            print(f"Error: Elevator {elevator_num} does not exist.")

    def fire_alarm(self):
        print(f"\n*** !!! FIRE ALARM AlERT !!! ***")
        print(f"--- Moving all elevators to the bottom floor ({self.bottom_floor}) ---")
        for i, elevator in enumerate(self.elevators):
            print(f"\n*** Moving Elevator {i} to bottom floor ***")
            elevator.go_to_floor(self.bottom_floor)
        print("\n--- All elevators are now at the bottom floor. ---")


if __name__ == "__main__":
    print("--- Creating a building with 3 elevators (floors 1-10) ---")
    my_building = Building(bottom_floor=1, top_floor=10, num_elevators=3)

    my_building.run_elevator(elevator_num=0, target_floor=7)
    my_building.run_elevator(elevator_num=1, target_floor=5)
    my_building.run_elevator(elevator_num=2, target_floor=9)

    my_building.fire_alarm()