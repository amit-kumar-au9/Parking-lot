class ParkingLot:
    def __init__(self, total_space, no_floor=1):
        self.parking = {}
        self.total_car = 0
        self.total_slot = total_space
        total_space = int(total_space)
        no_floor = int(no_floor)
        i, j = 1, 1
        while (i <= total_space and j <= no_floor):
            self.parking[('Floor' + str(j) + 'Slot' + str(i)).lower()] = []
            i += 1
            if i == total_space:
                j += 1
        print("Created a parking lot with", total_space * no_floor, "slots")

    def ParkCar(self, regno, color, email):
        current_time = datetime.now().time()
        for key, values in self.parking.items():
            if values == []:
                values.append(regno)
                values.append(color)
                values.append(current_time)
                values.append(email)
                print("Allocated slot number: ", key)
                self.total_car += 1
                return

    def LeaveParkingSlot(self, slot):
        if slot in self.parking.keys():
            if self.parking[slot] != []:
                car_data = self.parking[slot]
                start = car_data[2]
                email = car_data[3]
                self.sendEmail(email)
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
        print("Slot No. Registration No Colour Entry_Time Duration Email")
        for key, values in self.parking.items():
            if values != []:
                start = values[2]
                end = datetime.now().time()
                t1 = timedelta(hours=start.hour,
                               minutes=start.minute, seconds=start.second)
                t2 = timedelta(
                    hours=end.hour, minutes=end.minute, seconds=end.second)
                duration = t2 - t1
                print(key, values[0], values[1],
                      values[2].strftime("%H:%M:%S"), duration, values[3])

    def isNotFull(self):
        return 1 if self.total_car != self.total_slot else 0

    def isEmpty(self):
        return 1 if self.total_car == 0 else 0

    def carNotExist(self, regno):
        for values in self.parking:
            if values != []:
                if values[0] == regno:
                    return 0
        return 1

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

    def sendEmail(self, email):
        gmail_user = 'anonymous.people.one@gmail.com'
        gmail_password = 'slxfyyaaemsukkdv'

        sent_from = gmail_user
        to = [email]
        subject = 'Parking Lot Invoice'
        body = 'This is a testing mail'

        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, ", ".join(to), subject, body)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()
            print('Email sent!')
        except Exception:
            print('Something went wrong...')


def isEmailValid(email):
    regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    if(re.search(regex, email)):
        return 1
    else:
        return 0


if __name__ == "__main__":
    from datetime import datetime, timedelta
    import re
    import smtplib

    a = int(input("1 for Terminal Input and 2 for Executing File"))
    if a == 2:
        input_file = open(
            "D:/Technical Stuffs/Attainu Course/Parking-lot/file.txt", "r")
    while(True):

        if (a == 1):
            take = input().lower().split(" ")
        elif (a == 2):
            all_input_lines = input_file.readline()
            all_input_lines = all_input_lines.lower().replace('\n', '')
            take = all_input_lines.split(" ")
            if take[0] == '':
                break
        try:
            if take[0] == 'create_parking_lot':
                NewParking = ParkingLot(take[1])

            elif take[0] == 'park':
                if(NewParking.isNotFull()):
                    if NewParking.carNotExist(take[1]):
                        if isEmailValid(take[3]):
                            NewParking.ParkCar(take[1], take[2], take[3])
                        else:
                            print("Email address is not valid")
                    else:
                        print("Sorry, Same Car Already Park")
                else:
                    print("Sorry, parking lot is full")

            elif take[0] == 'leave':
                if(NewParking.isEmpty()):
                    print("Parking Slot is Empty")
                else:
                    NewParking.LeaveParkingSlot(take[1])

            elif take[0] == 'status':
                if(NewParking.isEmpty()):
                    print("Parking Slot is Empty")
                else:
                    NewParking.PrintParkingLot()

            elif take[0] == 'registration_numbers_for_cars_with_colour':
                if(NewParking.isEmpty()):
                    print("Parking Slot is Empty")
                else:
                    NewParking.FetchRegNoByColor(take[1])

            elif take[0] == 'slot_numbers_for_cars_with_colour':
                if(NewParking.isEmpty()):
                    print("Parking Slot is Empty")
                else:
                    NewParking.FetchSlotByColor(take[1])

            elif take[0] == 'slot_number_for_registration_number':
                if(NewParking.isEmpty()):
                    print("Parking Slot is Empty")
                else:
                    NewParking.FetchSlotByRegNo(take[1])

            elif take[0] == 'exit':
                break
        except Exception:
            print("Wrong input || Error Occured")
    if a == 2:
        input_file.close()
