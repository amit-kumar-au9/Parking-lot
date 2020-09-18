# PARKING LOT PROJECT

## DESCRIPTION

This is a parking lot project whose aim is to reduce human intervention and to make it an automatic process.

In this project, I have made a parking solution for parking owner/admin.

The project can handle multi-floor parking.

The parking spaces are being stored in the **Dictionary** datatype storing the slot_no as key and the car info as values

The car info is again stored in the form of **Dictionary** data type having a key and its value

_For eg:_

Parking Slot would be like = {'slot_no': Car_info OR Empty, 'slot_no': Car_info OR Empty, 'slot_no': Car_info OR Empty, ... So on}

Car Info would be like = {'regno': 'KA-01-HH-1234', 'color': 'White', 'current_time': '08:31:06', 'email': 'xyz@gmail.com'}

Empty/No Car would be like an empty dictionary = {}

---

## FEATURE

It has some basic listed features:

1. Create a Parking lot

2. Park new car

3. Leave a car

4. Check Status of Parking Lot

5. Search Car Registration No. by car Color

6. Search car Slot No. by car color

7. Search car Slot No. by car Registration No.

Extra Features:

1. Making it multi-floor parking having several floors

2. Storing entry time of the car and email address of the car owner

3. Checking car parking duration while checking the status of Parking Lot

4. Getting an E-mail notification while leaving the parking lot about your time duration and other details.

---

## EXPLAINING COMMANDS

| Feature                             | Command                                                              | Eg                                                |
| ----------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------- |
| Create Parking                      | create_parking_lot(space)(no of slot per floor)(space)(no of floor)  | create_parking_lot 6 1                            |
| Check Parking Lot Status            | status                                                               | status                                            |
| Park a new car                      | park(space)(registration no)(space)(car color)(space)(email address) | park KA-01-HH-1234 White amitkumar66966@gmail.com |
| Leave a car                         | leave(space)(slot no)                                                | leave Floor1Slot4                                 |
| Search registrtaion no. by color    | registration_numbers_for_cars_with_colour(space)(Car color)          | registration_numbers_for_cars_with_colour White   |
| Search slot no. by color            | slot_numbers_for_cars_with_colour(space)(Car Color)                  | slot_numbers_for_cars_with_colour White           |
| Search slot no. by registration no. | slot_number_for_registration_number(space)(Registration No.)         | slot_number_for_registration_number KA-01-HH-1234 |

---

## USAGE

Just go to through the main.py and run the code

This will show you an option of selecting among 2 choices i.e. Running Terminal Commands by Press 1 || Running commands saved on file.txt by Press 2

By choosing 1 you can type the commands and the resultant output would be there

By choosing 2 the file.txt will run and print the output of each command.

---

## AUTHOR

AMIT KUMAR

---
