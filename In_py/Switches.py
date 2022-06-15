Days = []
Days2 = []
Options = [1,2,3,4,5,6,7,100]
DaysOfWeek = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
    }
print("Enter the Days of the week using Digits")
print("1: Monday")
print("2: Tuesday")
print("3: Wednesday")
print("4: Thursda")
print("5: Friday")
print("6: Saturday")
print("7: Sunday")
print("Enter 100 if you are done")

# I will do This using Match switch Method and Dict Mapping Method

# MATCH SWITCH METHOD
# MACHINE 1 #
print("Machine 1")
while True:
    Chosen = int(input("Enter Your choosen Day: "))
    if Chosen in Options:
        match Chosen:
            case 1:
                Days.append(DaysOfWeek[1])
            case 2:
                Days.append(DaysOfWeek[2])
            case 3:
                Days.append(DaysOfWeek[3])
            case 4:
                Days.append(DaysOfWeek[4])
            case 5:
                Days.append(DaysOfWeek[5])
            case 6:
                Days.append(DaysOfWeek[6])
            case 7:
                Days.append(DaysOfWeek[7])
            case 100:
                break
    else:
        print("Incorrect Input Try the following")
        print("1: Monday")
        print("2: Tuesday")
        print("3: Wednesday")
        print("4: Thursda")
        print("5: Friday")
        print("6: Saturday")
        print("7: Sunday")
        print("Enter 100 if you are done")
print(f"Your chosen days are {Days}")

# DICT MAPPING METHOD with if, elif and else
# MACHINE 2 #
def monday():
    Days2.append("Monday")
    return 0
def tuesday():
    Days2.append("Tuesday")
    return 0
def wednesday():
    Days2.append("Wednesday")
    return 0
def thursday():
    Days2.append("Thursday")
    return 0
def friday():
    Days2.append("Friday")
    return 0
def saturday():
    Days2.append("Saturday")
    return 0
def sunday():
    Days2.append("Sunday")
    return 0
def wrong():
    print("Incorrect Input Try the following")
    print("1: Monday")
    print("2: Tuesday")
    print("3: Wednesday")
    print("4: Thursda")
    print("5: Friday")
    print("6: Saturday")
    print("7: Sunday")
    print("Enter 100 if you are done")
    return 0
switcher = {
    1: monday,
    2: tuesday,
    3: wednesday,
    4: thursday,
    5: friday,
    6: saturday,
    7: sunday
    }

def switch(ChosenDay):
    return switcher.get(ChosenDay)()

print("Machine 2")
while True:
    Chosen = int(input("Enter Your choosen Day: "))
    if Chosen in Options:
        if Chosen == 1:
            switch(1)
        elif Chosen == 2:
            switch(2)
        elif Chosen == 3:
            switch(3)
        elif Chosen == 4:
            switch(4)
        elif Chosen == 5:
            switch(5)
        elif Chosen == 6:
            switch(6)
        elif Chosen == 7:
            switch(7)
        elif Chosen == 100:
            break
    else:
        wrong()
print(f"Your Chosen Days are {Days2}")

# while process wise the 'match-case' method is the same with just writing a bunch of 'if', 'elif' and 'else'
# It is much more simpler to write and do compare to other methods like the 'Dict Mapping' method
# You have to write more lines of code for other method compare to the 'match-case' method