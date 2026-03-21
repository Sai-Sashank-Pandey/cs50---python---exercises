#method-1 of using datatypes
x=int(input("What's x? "))
y=int(input("What's y? "))
z=x+y
print(z)

#method-2 of using data types
x=input("What's x? ")
y=input("What's y? ")
z=int(x)+int(y)
print(z)

#let's try with floats by using round
x=float(input("What's x? "))
y=float(input("What's y? "))
z=round(x+y)
print(z)

#another method using multiple datatypes
x=float(input("What's x? "))
y=float(input("What's y? "))
z=int(x+y)
print(z)

# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Create a rounded result
z = round(x + y)

# Print the formatted result
print(f"{z:,}")

