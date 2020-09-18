# PARKING LOT PROJECT

## DESCRIPTION

---

This is a parking lot project which aim is to reduce human intervention and to make it a automatic process.

In this Project I have made a parking solution for parking owner/admin.

The project can handle multi floor parking.

The parking spaces are being stored in the **Dictionary** data type storing the slot_no as key and the car info as values

The car info is again stored in the form of **Dictionay** data type having key and its value

_For eg:_

Parking Slot would be like = {'slot_no': Car_info OR Empty, 'slot_no': Car_info OR Empty, 'slot_no': Car_info OR Empty, ... So on}

Car Info would be like = {'regno': 'KA-01-HH-1234', 'color': 'White', 'current_time': '08:31:06', 'email': 'xyz@gmail.com'}

Empty/No Car would be like an empty dictionary = {}

---

## FEATURE

It has some basic listed features:

1. Create Parking lot

2. Park a new car

3. Leave a car

4. Check Status of Parking Lot

5. Search Car Registration No. by car Color

6. Search car Slot No. by car color

7. Search car Slot No. by car Registraion No.

Extra Features:

1. Making it multi floor parking having several floors

2. Storing entry time of car and email address of car owner

3. Checking car parking duration while checking the status of Parking Lot

4. Getting an E-mail notification while leaving the parking lot about your time duration and other details.

## EXPLAINING COMMANDS

| Feature                             | Command                                                 | Eg                                                |
| ----------------------------------- | ------------------------------------------------------- | ------------------------------------------------- |
| Create Parking                      | create_parking_lot 'no of slot per floor' 'no of floor' | create_parking_lot 6 1                            |
| Check Parking Lot Status            | status                                                  | status                                            |
| Park a new car                      | park 'registration no' 'car color' 'email address'      | park KA-01-HH-1234 White amitkumar66966@gmail.com |
| Leave a car                         | leave 'slot no'                                         | leave Floor1Slot4                                 |
| Search registrtaion no. by color    | registration_numbers_for_cars_with_colour 'Car color'   | registration_numbers_for_cars_with_colour White   |
| Search slot no. by color            | slot_numbers_for_cars_with_colour 'Car Color'           | slot_numbers_for_cars_with_colour White           |
| Search slot no. by registration no. | slot_number_for_registration_number 'Registration No.'  | slot_number_for_registration_number KA-01-HH-1234 |

## USAGE

---

Just go to through the main.py and run the code

This will show you an option of selecting among 2 choice i.e. Running Terminal Commands by Press 1 || Running commands saved on file.txt by Press 2

By choosing 1 you can type the commands and the resultant output would be there

By choosing 2 the file.txt will run and prints the output of each command.

### INPUT

1

create_parking_lot 6 1

status

park KA-01-HH-1234 White xyz@gmail.com

park KA-01-HH-9999 White xyz@gmail.com

park KA-01-BB-0001 Black xyz@gmail.com

park KA-01-HH-7777 Red xyz@gmail.com

park KA-01-HH-3141 Blue xyz@gmail.com

park KA-01-HH-3141 Black xyz@gmail.com

leave Floor1Slot4

status

park KA-01-P-333 White xyz@gmail.com

park DL-12-AA-9999 White xyz@gmail.com

registration_numbers_for_cars_with_colour White

slot_numbers_for_cars_with_colour White

slot_number_for_registration_number KA-01-HH-1234

slot_number_for_registration_number MH-04-AY-1111

### OUTPUT

Created a parking lot with 6 slots

Parking Slot is Empty

Allocated slot number: floor1slot1

Allocated slot number: floor1slot2

Allocated slot number: floor1slot3

Allocated slot number: floor1slot4

Allocated slot number: floor1slot5

Sorry, Same Car Already Park

Check Your Email for Bill Invoice

Slot number floor1slot4 is free.

Duration Parked 0:00:00

Slot No. Registration No Colour Entry_Time Duration Email

floor1slot1 ka-01-hh-1234 white 17:58:46 0:00:03 xyz@gmail.com

floor1slot2 ka-01-hh-9999 white 17:58:46 0:00:03 xyz@gmail.com

floor1slot3 ka-01-bb-0001 black 17:58:46 0:00:03 xyz@gmail.com

floor1slot5 ka-01-hh-3141 blue 17:58:46 0:00:03 xyz@gmail.com

Allocated slot number: floor1slot4

Allocated slot number: floor1slot6

ka-01-hh-1234, ka-01-hh-9999, ka-01-p-333, dl-12-aa-9999

floor1slot1, floor1slot2, floor1slot4, floor1slot6

floor1slot1

Not found

---

## AUTHOR

AMIT KUMAR
