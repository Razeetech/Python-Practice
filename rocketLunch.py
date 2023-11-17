print("missile launched")
print("Are you on course?")
response = input().lower()

if response == "yes":
    print("Target reached?")
    response2 = input().lower()
    if response2 == "yes":
        print("Blow the missile")
    elif response2 == "no":
        print("Stay on course")
elif response == "no":
    print("Get back on track")
    print("Are you on track now?")
    response3 = input().lower()
    if response3 == "yes":
        print("Stay on course, focus on the target")
    elif response3 == "no":
        print("Blow up the target")
