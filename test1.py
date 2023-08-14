






def getInfo():
    var1 = input("\nplease provide the first numeric value: ")
    var2 = input("\nplease provide the second numeric value: ")
    return var1,var2



def compute():
    go = True
    while go:
        var1,var2 = getInfo()
        try:
            var3 = int(var1) + int(var2)
            go = False
        except ValueError as e:
            print("{}: \n\nYou didnt provide a numeric value".format(e))
        except:
            print("\n\nOops, you provided a invalid input, program will close now!")
    print("{} + {} = {}".format(var1,var2,var3))









if  __name__ == "__main__":
    compute()





def divide_numbers(a, b):
    try:
        result = a / b
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    finally:
        print("Finally block executed.")

# Test the function with different inputs
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    divide_numbers(num1, num2)
except ValueError:
    print("Error: Invalid input. Please enter valid integers.")
