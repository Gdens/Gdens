question = "y"
while question != "n":
        name = input("What is your name? ")
        number = input("What is your number? ")
        email = input("What is your email? ")
        with open("contacts.txt","a") as file:
            file.write(f"{name} {number} {email}\n")
        while True:
            question = input("Add another contact? Y|n: ")
            if question == "y" or question == "" or question == "n":
                break
            else:
                print("You did not make a correct selection. Please use a 'y' or 'n'.")
                

