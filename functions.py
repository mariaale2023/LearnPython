import math

def  show_hello():
  print("Hello, this is a first fiunction \n\n")
print("testing mu fisrts defines function \n\n")


# invoking function
show_hello()
# invoking function again
show_hello()


# >>> dir()
# ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']

dir(math)
print( math.pi)

def triangle_area(a, b):
  return 0.5 * a * b

print(triangle_area(3, 6))
print("\n\n")

def cm(feet = 0,  inches = 0):
  inches_to_cm = inches * 2.54
  feet_to_cm = feet * 12 * 2.54
  return inches_to_cm + feet_to_cm
print(cm(5,8))
print(cm(feet= 5 , inches = 8))
print(cm(inches = 8, feet= 5)) # if write to the order way
print(cm(feet = 5))
print(cm(inches = 70 ))

print("\n\n")
print("---------------------")


def show_hello(param):
    print("Hello there, the number of times this "
          "function is called is {0}!!!\n\n".format(param))

counter = 0
print("Testing my second user defined function...\n\n")
counter += 1

show_hello(counter)

print("---------------------")
first_number = 6
second_number = 4

def show_difference(number_1, number_2):
  print("Fisrt number is {0}.\n"
        "second number is {1}.\n"
        "The differnce between them is {2}".format(number_1, number_2, (number_1 - number_2)))

# print(show_difference(first_number, second_number))
show_difference(first_number, second_number)
print("\n")

show_difference(13, 2)


print("---------------------")
print("SCOPE")

 
# score = 3
# def show_new_score():
#   score = score  + 1
#   print(score)

# show_new_score()

# print(score)

print("---------Other option------------")

# score = 3
# def show_new_score(parameter):
#   parameter = parameter  + 1
#   print("thi is parameter equal to {0}".format(parameter))
#   return parameter

# score = show_new_score(parameter)


score = 4
 
def get_new_score(param_score):
    param_score += 1
    print("You got another point...\n"
          "Your score is now {0}.\n"
          .format(param_score))
    return param_score
# some run code
x = int(input("insert a number"))
# invoking the function and using it to set the new score
score = x + get_new_score(score)
score = x + get_new_score(score)
score = x + get_new_score(score)

print("---------------------")
name = "Maria"

def show_name():
  name = "Ale"
  print(name)

print(show_name())
show_name()
print(name)