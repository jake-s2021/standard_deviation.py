import math



def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

while 1:
    n = input("n =")
    x = [] #holds all values in the set
    xth = 0 #temporary variable for accepting the set values
    xtot = 0 #variable to hold the sum of all values in the set squared
    xnaught = 0 #average
    if isfloat(n):
        n = float(n)

        while isfloat(xth) or xth is "": #enter a letter to exit the loop and start calculation
            xth = input("X's: ")
            if isfloat(xth):
                x.append(float(xth))

        xnaught = sum(x)/n

        for i in x:
            xtot = xtot+(i**2)

        

        s = math.sqrt((1/(n-1))*(xtot-(n*(xnaught**2)))) #formula for standard deviation

        print(s)
        print("\n")

    else:
        print("not a number")

  
    