class ParkingLot:
    def __init__(self, total_space):
        self.parking = {}
        self.total_car = 0
        self.total_slot = total_space
        for i in range(1, int(total_space)+1):
            self.parking[i] = []
        print("Created a parking lot with", total_space, "slots")

    def PrintParkingLot(self):
        if self.total_car == 0:
            print("Parking Slot is Empty")
            return
        print("Slot No. Registration No Colour")
        for key, values in self.parking.items():
            if values != []:
                print(key, values[0], values[1])


if __name__ == "__main__":
    while(True):
        take = input().split(" ")
        if take[0] == 'create_parking_lot':
            NewParking = ParkingLot(take[1])

        elif take[0] == 'status':
            NewParking.PrintParkingLot()

        elif take[0] == 'exit':
            break

        else:
            print("Wrong input")
