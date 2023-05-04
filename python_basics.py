# Take user input for name, age, and degree program
name = input("What is your name? ")
age = int(input("How old are you? "))
degree_program = input("What is your degree program? ")

# Calculate remaining age
remaining_age = (age * 3) % 2

# Print message using string concatenation
print("Hello, my name is " + name + ". My remaining age is " + str(remaining_age) + " and I am currently studying " + degree_program + ".")
