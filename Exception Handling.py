try:
   
                firstnumber=int(input("Enter your first number"))
                secondnumber=int(input("Enter your second number"))
                Result=firstnumber/secondnumber
                print(Result)
                file=open("abc.txt","r")
except ValueError:
    print("Please enter Integer values only")
except ZeroDivisionError:
    print("Division by Zero is not possible")
except FileNotFoundError:
    print("This file does not exist")
