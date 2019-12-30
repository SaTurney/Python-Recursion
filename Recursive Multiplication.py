#Sabrina Turney
#November 6, 2018
#Recursive Multiplication
#This program asks the user for the input of two numbers and then calls a
#recursive module to multiply them together. The result is then displayed to
#the user and the code is able to loop. The exercise specified nonzero integers,
#but I made a full program that can also calculate with negatives (because it
#was only two extra lines of code).

#A small intro module to explain to the user what we're doing.
def intro():
    print("Welcome to my recursive multiplication calculator!")
    print("Please enter two numbers that will be multiplied together,")
    print("and then their product will be returned to you!")

#The main function. Looping and declarations take place here, as well
#as getting the user's input.
def main():

    #I declare the two variables we'll be inputting here and our loop.
    x = 0
    y = 0
    loopProgram = "yes"

    #Using a while loop to allow the program to be reusable:
    while loopProgram == "yes":
        x = 0
        y = 0

        #I call the intro module
        intro()

        #Get the two inputs from the user to multiply here
        x = int(input("\nPlease enter a number to multiply: "))
        y = int(input("Now, please enter a second number to multiply by: "))


        #I don't know the answer yet, but I will as soon as I call the
        #recursive module. I print out the user's numbers, and call the
        #module in giving them the product.
        print("\nThe product of these two numbers")
        print(f"you've entered, {x} and {y},") 
        print("is: ", multiply(x, y))

        #Here is where the user decides if they'd like to loop again.
        print("\nWould you like to use this calculator again?")
        loopProgram = input("Please enter yes or no: ")
        if loopProgram != "yes":
            print("\nThank you for using my program! Goodbye!")

#Here is the recursive module. I named it pretty aptly so I wouldn't get
#confused when calling it in my print function above.
def multiply(x, y):
    if (x < 0):
        #If the input is negative, our variables need to be multiplied
        #by negative one to retain the correct product.
        x = x * -1
        y = y * -1
    if (x > 0):
        #If x is greater than zero, we run our recursion, which runs through
        #iterations of y and x until x becomes zero.
        return y + multiply(x - 1, y)
    elif (y == 0) or (x == 0):
        #If we have a zero, it returns zero.
        return 0
    
#As is tradition, we call the main function for the user.
main()
