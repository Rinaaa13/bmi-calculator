inputage = int(input("Enter your age: "))

if inputage >= 18:
    print("You are old enough to learn to drive.")
else:
    years_to_wait = 18 - inputage
    print("You need {} more years to learn to drive.".format(years_to_wait))