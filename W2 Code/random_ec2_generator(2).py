#EC2 Random Name Generator

#welcome user and collect name
print("Hello, welcome to the EC2 Generator!")
name = input("May I have your first name please?\n")
name = (name.capitalize())
print("Thank you, " + name + (".") + (" Nice to meet you."))

#get the users department name
dept = input("What department do you work in, " + name + ("?") + (" Accounting, Marketing, or FinOps?\n")).upper()

#user needs to be in an approved department
while True:
    try:
        list = ["ACCOUNTING", "MARKETING", "FINOPS"]
        if dept not in list:
            raise ValueError
        
    except ValueError:
        print("I'm sorry, we don't support that department " + name + (".") + (" Please check in with your supervisor."))
        exit()
    else: 
        print("Thanks.")
        break
        
#get the number of unique EC2 names the user wants
while True:
    try:
        instnumb = int(input("How many instances do you need? "))
        print("Great! We'll get you those " + str(instnumb) + (" instances right away."))
        print("Here you go:")
        break
    except ValueError:
        print("Oops, looks like you hit the wrong key. Give that another try.")
        continue
    else:
        break
    
#random letters and digits that will follow the department name will be generated
import string
import random
n = instnumb
N = 3

for _ in range(n):
    custom_id = str(''.join([random.choice(string.ascii_letters + string.digits) for instnumb in range(10)]))
    print('{}-{}'.format(dept[0 : N], custom_id))
    
print(("Thanks for stopping by, ") + name + (". Take care."))
