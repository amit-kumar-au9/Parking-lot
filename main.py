class ParkingLot:
    def __init__(self, total_space):
        self.parking = {}
        self.total_car = 0
        self.total_slot = total_space
        for i in range(1, int(total_space)+1):
            self.parking[i] = []
        print("Created a parking lot with", total_space, "slots")

    def ParkCar(self, regno, color):
        for key, values in self.parking.items():
            if values == []:
                values.append(regno)
                values.append(color)
                print("Allocated slot number: ", key)
                self.total_car += 1
                return
        print("Sorry, parking lot is full")

    def LeaveParkingSlot(self, slot):
        if self.parking[int(slot)] != []:
            self.parking[int(slot)] = []
            print("Slot number", slot, "is free")
            self.total_car -= 1
        else:
            print("Slot number", slot, "is already free")

    def PrintParkingLot(self):
        if self.total_car == 0:
            print("Parking Slot is Empty")
            return
        print("Slot No. Registration No Colour")
        for key, values in self.parking.items():
            if values != []:
                print(key, values[0], values[1])

    def FetchRegNoByColor(self, color):
        notFound = True
        for key, values in self.parking.items():
            if self.parking[key] != []:
                if self.parking[key][1] == color:
                    if notFound:
                        print(values[0], end="")
                        notFound = False
                    else:
                        print(",", values[0])
        if notFound:
            print("Not found")

    def FetchSlotByColor(self, color):
        notFound = True
        for key, values in self.parking.items():
            if self.parking[key] != []:
                if self.parking[key][1] == color:
                    if notFound:
                        print(key, end="")
                        notFound = False
                    else:
                        print(",", key)
        if notFound:
            print("Not found")

    def FetchSlotByRegNo(self, regno):
        for key, values in self.parking.items():
            if values != []:
                if values[0] == regno:
                    print(key)
                    return
        print("Not found")


if __name__ == "__main__":
    while(True):
        take = input().split(" ")
        if take[0] == 'create_parking_lot':
            NewParking = ParkingLot(take[1])

        elif take[0] == 'park':
            NewParking.ParkCar(take[1], take[2])

        elif take[0] == 'leave':
            NewParking.LeaveParkingSlot(take[1])

        elif take[0] == 'status':
            NewParking.PrintParkingLot()

        elif take[0] == 'registration_numbers_for_cars_with_colour':
            NewParking.FetchRegNoByColor(take[1])

        elif take[0] == 'slot_numbers_for_cars_with_colour':
            NewParking.FetchSlotByColor(take[1])

        elif take[0] == 'slot_number_for_registration_number':
            NewParking.FetchSlotByRegNo(take[1])

        elif take[0] == 'exit':
            break

        else:
            print("Wrong input")
