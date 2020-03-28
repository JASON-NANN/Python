# quadratic4.py
import math
def main():
    print("Let us finds the solutions to a quadratic\n")
    a,b,c = eval(input("Do enter the coefficients(a,b,c):\n"))
    delta =b*b - 4*a*c
    if a == 0 :
        x = -b/c
        print("This is a solution:\n",x)
    elif delta < 0:
        print("The equation has no real roots!\n")
    elif delta == 0:
        x = -b /(2*a)
        print("There is a double root at:\n",x)
    else:
        discRoot = math.sqrt(delta)
        x1=(-b + discRoot) / (2*a)
        x2=(-b - discRoot) / (2*a)
        print("The solutions are:\n",x1 ,x2)
main()

        
    
        
        