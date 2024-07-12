import re
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[a-z]+(\.[A-Za-z]{2,})+')
def isValid(email):
    if re.fullmatch(regex, email):
      print("Valid email")
    else:
      print("Invalid email")

isValid("name.surname@gmail.com")
isValid("amortadas99@gmail.com")
isValid("anonymous123@yahoo.co.uk")
isValid("anonymous123+uk@yahoo.co.uk")
isValid("anonymous123@...uk")
isValid("...@domain.us")