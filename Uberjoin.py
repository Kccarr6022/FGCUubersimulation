# Kaden Carr
#Uberjoin ­ A model of Uber on Python. The following application will provide a transportation system specifically designed for
# the Florida Gulf Coast University campus. When the user enters the application they will be prompted to login, once logged in
# various destinations and starting positions will be given to the user. Once the location and destination is selected, the user
# will recieve a calculation for the total cost per mile of the service and the purchase will be sent by email to both parties.
­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­
import sys


# Cost of services (Variable initializations)
budget = 100
distance = 0
tax = 0.07
percent_cut = 0.05
driver_fee = 2
cost_per_mile = 1.25
tip_to_driver = 0


# Email sample
register_email = "Kccarr6022@eagle.fgcu.edu"


# Model of a personalized login system (Prototype)
selction_screen = "0"
while selction_screen != "Y" and selction_screen != "R":
    selction_screen = input("Press Y to continue with a registered account or R to register an account: ")


#Storing new account (add email options and database)
if selction_screen == "R":
    new_email = input("Enter the email you want to register this account with: ")
    new_username = input("Register a username: ")
    new_password = input("Register a password:")
    print("Welcome " + new_username + "!")


# No users in system currently (user database coming soon)
password_count = 0
register_username = input("Enter your username: ")
register_password = input("Enter your password: ")
print("Login Successfull")
print("Welcome back ", register_username + "!")


#Restarts process if user selects "N" to confirm destination
confirmation_destination = "Y"
while confirmation_destination == "Y":


    #Locations at Florida Gulf Coast University
    print("­" * 2 ** 4)
    print("01 = South Village")
    print("02 = North Village")
    print("03 = Main Campus")
    print("04 = Target")
    print("05 = Softball/Soccer Feilds")
    print("06 = University Village Shops")
    print("07 = Student Health Services")
    print("­" * 2 ** 4)


    #Prevents continuation with invalid information
    #crashes when pressing enter without input.
    starting = 0
    while starting < 1 or starting > 7:
        starting = int(input("Select your starting position(Must be a number 1­7): "))


    #Assigns a name based on user input
    if starting == 1:
        starting_name = "South Village"
    elif starting == 2:
        starting_name = "North Village"
    elif starting == 3:
        starting_name = "Main Campus"
    elif starting == 4:
        starting_name = "Target"
    elif starting == 5:
        starting_name = "Softball/Soccer Feilds"
    elif starting == 6:
        starting_name = "University Village Shops"
    else:
        starting_name = "Student Health Services"


    #Include a prompt of continuation
    print("­" * 2 ** 4)
    print("You have selected",starting_name)
    print("­" * 2 ** 4)
    print("01 = South Village")
    print("02 = North Village")
    print("03 = Main Campus")
    print("04 = Target")
    print("05 = Softball/Soccer Feilds")
    print("06 = University Village Shops")
    print("07 = Student Health Services")
    print("­" * 2 ** 4)


    destination = 0
    while destination < 1 or destination > 7:
        destination = int(input("Select your destination(Must be a number 1­7): "))
        # Assigns name based on selection
        if destination == 1:
            destination_name = "South Village"
        elif destination == 2:
            destination_name = "North Village"
        elif destination == 3:
            destination_name = "Main Campus"
        elif destination == 4:
            destination_name = "Target"
        elif destination == 5:
            destination_name = "Softball/Soccer Feilds"
        elif destination == 6:
            destination_name = "University Village Shops"
        else:
            destination_name = "Student Health Services"


    #Destination vs starting Position distance


    #Calculations
    price_per_miles = distance * cost_per_mile
    total_price = ((distance * cost_per_mile) + driver_fee) + percent_cut * ((distance* cost_per_mile) + driver_fee) + tax * ((distance * cost_per_mile) + driver_fee) + tip_to_driver
    change = total_price % budget
    string_price_per_miles= "${:,.2f}".format(price_per_miles)
    string_price = "${:,.2f}".format(total_price)
    string_change = "${:,.2f}".format(total_price)


    #Prints expenses for service
    print("Total cost of trip: " + string_price)
    print("Total cost: " + str(total_price))
    print("Change: ", string_change)
    print("­" * 2 ** 4)


    #Confirm destination here
    confirmation_destinations = input(starting_name + " to " + destination_name + "? Y/N: ")
    while confirmation_destinations != "Y" and confirmation_destinations != "N":
        confirmation_destinations = input(starting_name + " to " + destination_name + "? Y/N: ")
        #https://stackoverflow.com/questions/73663/how­to­terminate­a­python­script
    if confirmation_destinations == "Y":
        valid_password = input("Reenter your password: ")
        if valid_password == register_password:
            print("A confirmation email will be sent to " + register_email + ".")
            break
        while valid_password != register_password:
            valid_password = input("Password for user " + register_username + ":")
            password_count += 1
            print("You have " + str(password_count) + " out of 3 attempts used")
            if password_count == 3:
                print("You have used 3 of 3 password attemps")
                #Work on fixing the exit statement
                sys.exit("You have used all three password attemps.")