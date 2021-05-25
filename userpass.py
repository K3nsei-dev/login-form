# username and password program
# username information
username = ["Jeandre", "Justin", "Abdullah", "Jesse", "Thabo"]
# password information
password = ["1234", "2345", "3456", "4567", "5678"]

# input values
x = input("Enter your username:")
y =input("Enter your password:")
found = False

# function to run the program
for z in range(len(username)):
    if x == username[z] and y == password[z]:
        found = True

# to print the statement
if found == True:
    print ("Access Granted")
else:
    print("Access Denied")
