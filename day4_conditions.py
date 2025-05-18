age = int(input("What is your age?:"))
if age < 18:
    print("You are a minor")
elif age == 18:
    print("You are exactly 18 - legal adult")
else:
    print("You are an adult")
if age >= 18:
    has_license = input("Do you have a driving license? (yes/no):").lower()

if has_license == "yes":
    print ("You can legally drive")
else:
    print("You cannot legally drive yet")