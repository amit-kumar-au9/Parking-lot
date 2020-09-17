class ParkingLot:
    def __init__(self, total_space, no_floor=2):
        self.parking = {}
        total_space = int(total_space)
        no_floor = int(no_floor)
        i, j = 1, 1
        while (j <= no_floor):
            self.parking[('Floor' + str(j) + 'Slot' + str(i)).lower()] = {}
            if i == total_space:
                j += 1
                i = 1
            else:
                i += 1
        print("Created a parking lot with", len(self.parking), "slots")
        self.total_car = 0
        self.total_slot = len(self.parking)

    def ParkCar(self, regno, color, email):
        current_time = datetime.now().time()
        for key, values in self.parking.items():
            if values == {}:
                values['regno'] = regno
                values['color'] = color
                values['current_time'] = current_time
                values['email'] = email

                print("Allocated slot number: ", key)
                self.total_car += 1
                return

    def LeaveParkingSlot(self, slot):
        if slot in self.parking.keys():
            if self.parking[slot] != {}:
                car_data = self.parking[slot]
                duration = self.timeDuration(car_data['current_time'])
                sendEmail(car_data['regno'],
                          car_data['color'], duration, car_data['email'])
                print("Slot number", slot, "is free.")
                print("Duration Parked", duration)
                self.total_car -= 1
                self.parking[slot] = {}
            else:
                print("Slot number", slot, "is already free")
        else:
            print("Slot number", slot, "is not Present")

    def timeDuration(self, start):
        end = datetime.now().time()
        t1 = timedelta(hours=start.hour,
                       minutes=start.minute, seconds=start.second)
        t2 = timedelta(
            hours=end.hour, minutes=end.minute, seconds=end.second)
        return t2 - t1

    def PrintParkingLot(self):
        print("Slot No. Registration No Colour Entry_Time Duration Email")
        for key, values in self.parking.items():
            if values != {}:
                duration = self.timeDuration(values['current_time'])
                curr_time = values['current_time'].strftime("%H:%M:%S")
                print(key, values['regno'], values['color'],
                      curr_time, duration, values['email'])

    def FetchRegNoByColor(self, color):
        notFound = True
        for key, values in self.parking.items():
            if self.parking[key] != {}:
                if self.parking[key]['color'] == color:
                    if notFound:
                        print(values['regno'], end="")
                        notFound = False
                    else:
                        print(",", values['regno'])
        if notFound:
            print("Not found")

    def FetchSlotByColor(self, color):
        notFound = True
        for key in self.parking:
            if self.parking[key] != {}:
                if self.parking[key]['color'] == color:
                    if notFound:
                        print(key, end="")
                        notFound = False
                    else:
                        print(",", key)
        if notFound:
            print("Not found")

    def FetchSlotByRegNo(self, regno):
        for key, values in self.parking.items():
            if values != {}:
                if values['regno'] == regno:
                    print(key)
                    return
        print("Not found")

    def isNotFull(self):
        return 1 if self.total_car != self.total_slot else 0

    def isEmpty(self):
        return 1 if self.total_car == 0 else 0

    def carNotExist(self, regno):
        for key in self.parking:
            if self.parking[str(key)] != {}:
                if self.parking[str(key)]['regno'] == regno:
                    return 0
        return 1


def sendEmail(regno, color, duration, receiver):
    sender = 'anonymous.people.one@gmail.com'
    password = 'slxfyyaaemsukkdv'
    message = MIMEMultipart("alternative")
    message["Subject"] = "Car Parking Checkout"
    message["From"] = 'Car Parking'
    message["To"] = receiver
    regno = regno.upper()
    color = color.upper()
    # write the plain text part
    text = """\
    Hi User,
    Check out the details of your car parking:
    Registration Number :{}
    Color :{}
    Duration :{}

    Feel free to let us know for any query!
    We Hope To See You Soon
    Thank You
    """.format(regno, color, duration)
    # write the HTML part
    html = """\
    <html>
    <body>
        <h3 style='color:#4472C4;'>Hi User,</h3>
        <p>Check out the details of your car parking:&nbsp;&nbsp;&nbsp;</p>
        <p><strong>Registration Number : </strong>{}</p>
        <p><strong>Color : </strong>{}</p>
        <p><strong>Duration : </strong>{}</p>
        <p><strong>&nbsp;</strong></p>
        <p style='color:green;'>Feel free to let us know for any query!</p>
        <p style='color:green;'>We Hope To See You Soon Again</p>
        <p><em style='color:red;'><b>Thank You</b></em></p>
    </body>
    </html>
    """.format(regno, color, duration)
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(sender, password)
        server.sendmail(sender, receiver, message.as_string())
        server.close()
        print('Check Your Email for Bill Invoice')
    except Exception:
        print('Error Occured while sending email')


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
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

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
                NewParking = ParkingLot(take[1], take[2])

            elif take[0] == 'park':
                if NewParking.isNotFull():
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
            print()
        except Exception:
            print("Wrong input || Error Occured")
    if a == 2:
        input_file.close()
