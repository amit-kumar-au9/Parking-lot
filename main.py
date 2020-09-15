class ParkingLot:
    def __init__(self, total_space, no_floor=1):
        self.parking = {}
        self.total_car = 0
        self.total_slot = total_space
        total_space = int(total_space)
        no_floor = int(no_floor)
        i, j = 1, 1
        while (i <= total_space and j <= no_floor):
            self.parking['Floor' + str(j) + 'Slot' + str(i)] = []
            i += 1
            if i == total_space:
                j += 1
        print("Created a parking lot with", total_space * no_floor, "slots")

    def ParkCar(self, regno, color):
        current_time = datetime.now().time()
        for key, values in self.parking.items():
            if values == []:
                values.append(regno)
                values.append(color)
                values.append(current_time)
                print("Allocated slot number: ", key)
                self.total_car += 1
                return
        print("Sorry, parking lot is full")

    def LeaveParkingSlot(self, slot):
        if slot in self.parking.keys():
            if self.parking[slot] != []:
                start = self.parking[slot]
                start = start[2]
                end = datetime.now().time()
                t1 = timedelta(hours=start.hour,
                               minutes=start.minute, seconds=start.second)
                t2 = timedelta(
                    hours=end.hour, minutes=end.minute, seconds=end.second)
                duration = t2 - t1
                print("Slot number", slot, "is free.")
                print("Duration Parked", duration)
                self.total_car -= 1
                self.parking[slot] = []
            else:
                print("Slot number", slot, "is already free")
        else:
            print("Slot number", slot, "is not Present")

    def PrintParkingLot(self):
        if self.total_car == 0:
            print("Parking Slot is Empty")
            return
        print("Slot No. Registration No Colour Entry_Time Duration")
        for key, values in self.parking.items():
            if values != []:
                start = values[2]
                end = datetime.now().time()
                t1 = timedelta(hours=start.hour,
                               minutes=start.minute, seconds=start.second)
                t2 = timedelta(
                    hours=end.hour, minutes=end.minute, seconds=end.second)
                duration = t2 - t1
                print(key, values[0], values[1], values[2], duration)

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
        for key in self.parking:
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
    from datetime import datetime, timedelta
    a = int(input("Press 1 for Interative commands & Press 2 for File Commands: "))
    if a == 2:
        input_file = open(
            "D:/Technical Stuffs/Attainu Course/Parking-lot/file.txt", "r")
    while(True):

        if (a == 1):
            take = input().split(" ")
        elif (a == 2):
            all_input_lines = input_file.readline()
            all_input_lines = all_input_lines.replace('\n', '')
            take = all_input_lines.split(" ")
            if take[0] == '':
                break

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
            break
    if a == 2:
        input_file.close()
