#This is my first program
# print("Hello World!")
# print("Your mom")
# print()
# print("2+3")
# print(2+3)
# print("Hello World")
# print("2"+"3")
# print("Your new score is",1030 +23)
# print("Your new score is ","1030+23")
# #print("Your new score is,""1030)
# print("Your new score is,",1030+23)
# print("Hello", "World")
# print("I want to print a double quote for some reason", end=" Hello")
# print("Goodbye")
# print("Hello Again")

# miles_drive = int(input("Enter miles driven: "))
# gallons_used = float(input("Enter gallons used: "))
# mpg = miles_drive/gallons_used
# print(mpg)

# print("Hello my name is \rTommy")
# print("\nHello my name is Tommy")

n = 6
stop = 6
def divisor_sum(n):
    total = 0
    for divisor in range(1, n):
        if n % divisor == 0:
            total += divisor
    return total

def is_perfect(n):
    return n != 0 and n == divisor_sum(n)

def find_perfects(stop):
    for num in range(1, stop):
        if is_perfect(num):
            print("Found perfect number: ", num)
        if num % 10000 == 0: print('.', end='',flush=True) # progress bar
    print("Done searching up to ", stop)