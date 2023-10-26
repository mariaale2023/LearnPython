# is_running = True
 
# while is_running:
#     answer = input("What is the meaning of life?...\n")
#     if answer == "42":
#         print("Correct! Well done!\n")
#         # correct answer, so exit loop - reset is_running
#         is_running = False
#     else:
#         print("Sorry that is the wrong answer.... "
#               "Try again!\n")
 
# x = input("Press any key to exit.")

# ---------------------------------------------------------------------

# number_of_tries = 3

# while True:
#   answer = input("What is the menaing of life..\n")
#   if answer == "Dead":
#     print("Correct")
#     # how the answer is correct, exit the loop with break
#     break 
#   else: 
#     print("Sorry, try again...\n")
#     #number_of_tries = number_of_tries - 1 
#     number_of_tries -= 1

#   #check if number of tries and break if none left
#   if number_of_tries == 0:
#     print("You have run out of goes. sorry")
#     break

# x = input("Press Enter to exit.")


# ---------------------------------------------------------------------

name = ""
while len(name) == 0:
  name = input("Enter your name: ")

print (f"Hello {name}")
