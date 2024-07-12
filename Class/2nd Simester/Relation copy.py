import re

pattern = "[a-z0-9]+@[a-z]+\.[a-z]{2,3}$"
user_id=input("enter the email id: ")

if re.search(pattern, user_id):
  print("Valid email")
else:
  print("Invalid email")

