name = input("what is your name? ")
color = input("what is your favorite color? ")
age = int(input("how old are you? "))


# Remove the # on the next three lines to have script run on three lines
# print(name, end=" ")
# print("is " + str(age) + " years old", end=" ")
# print("and loves the color " + color + ".", end=" ")


# Add a # to the script below if running the three above. This one will all run on one line
print(name, 'is', age, 'years old and loves the color', color + '.', sep=" ")
