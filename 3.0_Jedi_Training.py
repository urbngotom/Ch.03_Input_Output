# 3.0 Jedi Training (20pts)  Name: Tommy Ngo


# In all the short programs below, do a good job communicating with your end user!


# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name. (1pt)
user_name = input("What is your name? ")
print("Welcome "+user_name+"!")

# 2. Write a program where a user enters a base and height and you print the area of a triangle. (1pt)
base = float(input("What is the base of triangle: "))
height = float(input("What is the height of the triangle: "))
area = 1/2*base*height
print("The area of the triangle is", area)

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference. (1pt)
circle_radius = float(input("What is the radius of the circle: "))
pi = 3.14
circumference = 2*pi*circle_radius
print("The circumference of the circle is", circumference)

# 4. Ask a user for an integer and then print the square root. (1pt)
integer = int(input("Pick an integer: "))
square_root = integer**(1/2)
print("The square root of the integer is", square_root)

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next. (1pt)
mass = float(input("What is the mass of your object? "))
acceleration = float(input("What is the acceleration of your object? "))
print("May the mass times acceleration be with you!")
force = mass*acceleration
print(force, "\nGet it?")
'''
6. TEMPERATURE PROGRAM (5pts)
-------------------
Create a program that asks the user for a temperature in Fahrenheit, and then prints the temperature in Celsius.

Test your program with the following data:

In: 32  Out: 0
In: 212  Out: 100
In: 52  Out: 11.1
In: 25  Out: -3.9
In: -40  Out: -40

'''
fahrenheit = float(input("Temperature in fahrenheit: "))
celsius = (fahrenheit-32)*5/9
print("The temperature in celsius is", celsius)

'''
7. TRAPEZOID PROGRAM (5pts)
-------------------
Create a new program that will ask the user for the information needed to find the area of a trapezoid, and then print the area.

Test with the following:

base 1: 2       base 2: 3    height: 4    area: 10
base 1: 5       base 2: 7    height: 2    area: 12
base 1: 1       base 2: 2    height: 3    area: 4.5
base 1: 7       base 2: 2    height: 4    area: 18
'''
base_one = int(input("Length of base 1 of the trapezoid: "))
base_two = int(input("Length of base 2 of the trapezoid: "))
height = int(input("Height of the trapezoid: "))
area = (base_one+base_two)/2*height
print("The area of the trapezoid is", area)
'''
8. GRADING PROGRAM (5pts)
---------------
Create a program that asks the user for their semester grade, final exam grade, 
and final exam worth and then calculates the overall final grade. 
Ask your instructor if you don't know how to calculate weighted averages.
You don't have to print out the letter grade. We will do that in the next chapter.

Test with the following:

Sem Grade: 86   Final Exam: 52   Exam worth: 15%    Overall: 80.9
Sem Grade: 95   Final Exam: 32   Exam worth: 10%    Overall: 88.7
Sem Grade: 72   Final Exam: 100   Exam worth: 20%    Overall: 77.6
'''
semester_grade = int(input("Your semester grade: "))
final_exam = int(input("Your final exam grade: "))
exam_worth = int(input("How much was your final exam worth? "))
overall_grade = semester_grade*((100-exam_worth)/100)+final_exam*(exam_worth/100)
print("Your overall grade is", overall_grade)





