
mascots = {
    "Michigan State": "Spartans",
    "Michigan": "Wolverines",
    "Wisconsin": "Badgers",
    "Ohio State": "Buckeyes",
    "Penn State": "Nittany Lions",
    "Indiana": "Hoosiers"
}

university = input("What university's mascot are you looking for? ")
if university in mascots:
    print("People who go to", university, "are called", mascots[university])
else:
    print("Mascot information not found for", university)


