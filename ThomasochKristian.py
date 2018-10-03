import os
import sys
import time


# Python program made by Thomas Touma and Kristian Obradovic

class pt:  # class used for ordering a workout plan

    def human(self):
        print("Name:", self.name, "\nAge:", self.age, "\nGender:", self.gender, "\nEmail:", self.mail)

    def training(self):
        print("You can choose between cardiovascular training 3 days a week \nor strength training 4 days a week ")
        self.workouttype = input("""Do you want to order a cardiovascular workout schedule [1] 
or a strength workout schedule[2]: """)


class TkGym:  # Creating a class called training with attributes and methods that are used in our loop systems

    def __init__(self):
        print("Hi and welcome to TK GYM AB")
        self.gymcard = input("Would you like to purchase a gym membership? yes/no: ")
        # instance that is used to determine a boolean value to a loop later on in code

    def membership(self):   # Creating a method that communicates with the user and take inputs for my different loops
        self.Name = input("Enter card holder name?: ")
        self.Lastname = input("Enter card holder last name?: ")
        self.email = input("Enter card holder email: ")

    def months(self):
        self.months = int(input("How many months would you like to be a member?: "))

    def user(self):
        print("Thank you for chosing us for", self.months, " months")


def createUser():
    # User enters their username, password, firstname and lastname that is saved down into a .txt file
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    firstname = input("Enter your first name: ")
    lastname = input("Enter your last name: ")
    username = username.strip()
    password = password.strip()
    firstname = firstname.strip()
    lastname = lastname.strip()
    file = open("mytest.txt", "a")
    file.write('\n')
    file.write(username)
    file.write(',')
    file.write(password)
    file.write(',')
    file.write(firstname)
    file.write(',')
    file.write(lastname)
    file.write('\n')
    file.close()


def isAuthorized():  # Method that is used for logging into an existing user by returning a boolean, true or false
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    for line in open("mytest.txt", "r"):    # opens mytest.txt and loops trough every line
        logininfo = line.strip().split(",")
        # strips down every line in mytest.txt into a list called logininfo and removes ","
        if username != logininfo[0] or password != logininfo[1]:
            continue
        elif username == logininfo[0] and password == logininfo[1]:
            print('welcome', logininfo[2], logininfo[3])
            return True  # sets the boolean value of the method isAuthorized to True if user is logged in
    return False     # sets the boolean value of the method isAuthorized to False if user isn't logged in


def menu():  # Menu method with 5 options that users can choose between
    val = input("""Hi and welcome to TK GYM AB\n 1. Create a user/or login \n 2. Buy a gymcard \n 3. Order a workout schedule \n 4. Bmi calculator
 5. Exit\n >>""")
    if val == "1":  # Creating a users by a while loop an also by calling the isauthorized method
        while True:  # This is the while loop that creates the user
            yesno = input("Do you want to create a user? yes/no: ")
            if yesno == 'yes':
                createUser()
                print('You will now proceed to login.')
                if isAuthorized():  # If the methods boolean value is set to True
                    input("Authorized \t Press any key to continue: ")  # prints that the user is authorized
                else:  # If the methods boolean value is set to False
                    input("Not authorized")   # prints that the user is not authorized
                break
            elif yesno == 'no':
                yesno = input("Do you already have a user? yes/no")
                if yesno == 'yes':
                    if isAuthorized():  # If the methods boolean value is set to True
                        input("Authorized \t Press any key to continue: ")
                    else:  # If the methods boolean value is set to False
                        input("Not authorized")
                    break
                elif yesno == 'no':
                    print("""It seems that you don't want to create a user nor do you have a user.
        Back to menu>>>""")
                    break
        menu()

    if val == "2":  # calling back the isauthorised method so yu can choose if you want a membership at TK Gym AB
        if isAuthorized():  # If the methods boolean value is set to True
            input("Authorized \t Press any key to continue: ")
            training1 = TkGym()
            if training1.gymcard != 'yes':
                print('We find it sad that you don\'t want to buy a gym membership\nReturning to main menu>>>')
                minloop1 = False
                menu()
            else:
                minloop1 = True

            while minloop1:  # This is the while loop that creates the membership and present different payment choices
                if training1.gymcard == 'yes':
                    training1.membership()
                    while True:
                        try:
                            training1.months()
                            break
                        except ValueError:
                            print('Invalid input try again')
                    training1.user()
                    while True:
                        try:
                            months = float(input("Confirm your months again: "))
                            break
                        except ValueError:
                            print('Invalid input try again')

                    yesno = input("Would you like to take a loan?" "yes/no ?: ")
                    monthlycost = 300  # Monthly cost for a gymcard
                    months1 = months * monthlycost # total cost for the users gymcard membership period
                    print("Your cost:", months1)
                    if yesno == "yes":
                        print("Proceed payment: ")
                        break
                    else:
                        minloop2 = True
                while minloop2:  # nested loop, that is set to true if the user want´s to pay directly
                    paychoice = input("Do you want to pay with master or visa?")
                    if (paychoice == "visa") or (paychoice == "master"):
                        print("Invoice has been send to you at " + training1.email)
                        break
                    else:
                        print("Something went wrong, error ")
                        break
                minloop1 = False

            if yesno != "yes":  # if the user doesn't want to take a loan this statement is called
                minloop = False  # sets the boolean value of minloop to False, so that the loop is never executed
            else:
                minloop = True   # sets the boolean value of minloop to True, so that the loop is executed
            allowed_income = 100000  # sets up the minimal income allowed to be able to lend money
            while minloop:  # minloop used for taking a loan
                while True:
                    try:
                        loan = int(input('How much would you like to lend? '))
                    except ValueError:
                        print('Invalid input try again')
                    try:
                        age = int(input('How old are you? '))
                    except ValueError:
                        print('Invalid input try again')
                    try:
                        income = int(input('Your income? minimal income is 100k: '))
                        break
                    except ValueError:
                        print('Invalid input try again')

                if (loan >= 1) and (loan <= 2999) and (age >= 18) and (income >= allowed_income):
                    interest = loan * 0.063  # calculates the users interest
                    print('Your loan:', loan)
                    print('Your interest:', interest)
                    print('Your total payment:', loan + interest)  # the total payment included with interest
                    break
                elif (loan >= 3000) and (loan <= 6000) and (age >= 18) and (income >= allowed_income):
                    interest = loan * 0.04  # calculates the users interest
                    print('Your loan:', loan)
                    print('Your interest:', interest)
                    print('Total payment:', loan + interest)  # the total payment included with interest
                    break
                elif age < 18:
                    print('You\'re to young to take a loan')
                    break
                elif income < allowed_income:
                    print("To low income")
                else:
                    print('You have entered a too high or low loan')
                    continue
            menu()
        else:  # if the boolean value of the user login credentials is not correct and set to False it executes the code
            input("Not authorized")
            menu()

    if val == "3":  # third choice in the menu, workout schedule generator
        if isAuthorized():  # promts the user to login and returns the boolean value either True or False
            input("Authorized \t Press any key to continue: ")
            print("""Hello and welcome to the workout schedule generator that will help you to create a workout plan.
Tailored to your own goals, on your own terms!
            """)
            pt1 = pt()

            while True:  # loop used for generating users workout plan
                pt1.training()
                if pt1.workouttype == "2":
                    print("""We find it incredibly rewarding that you've made the choice to order a workout schedule
adapted after strength training.""")
                    print("""YOUR WORKOUT SCHEDULE WILL FOLLOW DOWN BELOW.
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>""")
                    time.sleep(5)
                    print("""Day 1: Leg day
Excercise 1:
Squats 5 x 5 sets, rest 2 minutes

Excercise 2:
Quads 3 x 10 sets, rest 2 minutes

Excercise 3:
Leg press 5 x 5 sets, rest 2 minutes

Excercise 4:
Calves 4 x 10 sets, rest 2 minutes

Day 2: Back and chest

excercise 1:
Barbell Incline Bench Press Medium-Grip
4 sets, 8-10 reps (90 seconds rest) 

excercise 2 
Seated Cable Rows
Superset: 10 Minutes, alternating with Dumbbell Bench Press
1 set, 15-20 reps (wide-grip, minimal rest) 

excercise 3 
Dumbbell Bench Press
1 set, 15-20 reps (rest 2 minutes) 

excercise 4 
Decline Barbell Bench Press
Superset: 10 Minutes, alternating with Pullups
1 set, 12-15 reps (minimal rest) 

excercise 5 
Pullups or 12-15 pull-downs if you can't complete at least 5 pull-ups
1 set, to failure (2 minutes rest) 

Day 3: Lower Body (Hamstrings and Core) 
excercise 1 
Romanian Deadlift
4 sets, 8-10 reps (90 seconds rest) 

excercise 2 
Dumbbell Lunges
Superset: 10 Minutes, alternating with Lying Leg Curls
1 set, 16-20 reps (minimal rest) 

excercise 3 
Lying Leg Curls
1 set, 12-15 reps (rest 2 minutes) 

excercise 4 
Band Good Morning
Superset: 8 Minutes, alternating with Ab Roller
1 set, 15 reps (minimal rest) 

excercise 5 
Ab Roller
1 set, 12-15 reps (rest 2 minutes) 

Day 4: Shoulders and Arms
excercise 1 
Standing Military Press
4 sets, 8-10 reps (90 seconds rest) 

excercise 2 
Bradford/Rocky Presses
Superset: 8 Minutes, alternating with Rear Delt Raise
1 set, 12-15 reps (minimal rest) 

excercise 3 
Seated Bent-Over Rear Delt Raise
1 set, 15-20 reps 

excercise 4 
Close-Grip Barbell Bench Press
Superset: 8 Minutes, alternating with Barbell Curl
            1 set, 12-15 reps 

excercise 5 
Barbell Curl
1 set, 12-15 reps""")
                    print('Returning to main menu>>>>')
                    time.sleep(2)
                    menu()
                elif pt1.workouttype == "1":
                    print("""We find it incredibly rewarding that you've made the choice to order a workout schedule
adapted after cardiovascular training.""")
                    print("""YOUR WORKOUT SCHEDULE WILL FOLLOW DOWN BELOW.
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>""")
                    time.sleep(5)
                    print("""Day 1:
excercise 1:
Running 20 minutes
Powerwalk 30 minutes 

excercise 2:
intervals 20 minutes
Skipping 2 x 12 minutes 

Day 2:

excercise 1:
Skipping 5 minutes + 2 minutes plank 
5 sets 

excercise 2: 
Intervals 5 minutes + situps 2 minutes 
8 sets 

Day 3:

excercise 1:
Powerwalk 30 minutes

excercise 2:
Situps 5 sets - 20 reps

excercise 3:
Plank 2 minutes x 3 

excercise 4:
skipping 5 minutes x 3
""")
                    print('Returning to main menu>>>')
                    time.sleep(2)
                    menu()

                else:
                    print("""We find it sadly that you are not interested in any program we offer.
Returning to main menu>>>>""")
                    time.sleep(1.5)
                    menu()
        else:  # if the boolean value of the user login credentials is not correct and set to False it executes the code
            input("Not authorized")
            menu()
    if val == "4":  # calculates users bmi and calories intake, tells the user if it necessary to cut or get more calc
        print("We need to calculate your bmi and calorie intake")
        while True:
            try:
                lenght_cm = float(input("Enter your height, (Decimals, ex 1.85): "))  # used float for bmi
                break
            except ValueError:
                print("Invalid input try again")
        while True:
            try:
                weight_kg = float(input("Enter your weight: "))
                break
            except ValueError:
                print("Invalid input try again")

        bmi = weight_kg / (lenght_cm ** 2)
        while True:
            try:
                lenght = int(input("Enter your height, (integer, ex 185): "))  # used int for calories
                break
            except ValueError:
                print("Invalid input try again")
        while True:
            try:
                weight = int(input("Enter your weight: "))
                break
            except ValueError:
                print("Invalid input try again")
        while True:
            try:
                age = int(input("Your age: "))
                break
            except ValueError:
                print("Invalid input try again")

        calories = (+lenght * 6.23) + (+weight * 12.7) - (+age * 6.8) + 66

        if bmi < 18.5:
            print("Your bmi", bmi, " is underweight")
            print("Your daily calories are", calories, ". You need to eat 600 calories more per/day ")
            menu()
        if bmi <= 25:
            print("Your bmi", bmi, " is normal weight")
            print("Your daily calories are", calories, ". Your calories per/day are good ")
            menu()
        elif bmi >= 25.1:
            print("Your bmi", bmi, " is overweight ")
            print("Your daily calories are", calories, ". You need to cut 600 calories per/day ")
            menu()
        else:
            print("Something went wrong ")
            menu()
        print()

    if val == "5":  # choice 5 quits/exit the program
        print('Terminating program...')
        raise SystemExit()


menu()
