print("|--------+------=------sqr----Calculator in Python-----cub-----/--------*--------|") 

def calculator():
    while True:
        print("Enter '+' to add two numbers")
        print("Enter '-' to subtract two numbers")
        print("Enter '*' to multiply two numbers")
        print("Enter '/' to divide two numbers")
        print("Enter '%' to get modulus of two numbers")
        print("Enter 'sqr' to square of any number")
        print("Enter 'cube' to cube of any number")
        print("Enter 'quit' to end the program")
        

        user_input = input("")

        if user_input == "quit":
            break
    
        elif user_input in ["+", "-", "*", "/", "%"]:
            
            num1 = float(input("Enter a number: "))
           
            num2 = float(input("Enter another number: "))
        
        elif user_input in ["sqr", "cube"]:
            
            num1 = int(input("Enter a number: "))

        
            if user_input == "+":
                result = num1 + num2
                print(num1, "+", num2, "=", result)

            elif user_input == "-":
                result = num1 - num2
                print(num1, "-", num2, "=", result)

            elif user_input == "*":
                result = num1 * num2
                print(num1, "*", num2, "=", result)

            elif user_input == "/":
                result = num1 / num2
                print(num1, "/", num2, "=", result)
                
            elif user_input == "%":
                result = num1 % num2
                print(num1, "%", num2, "=", result)
                
            elif user_input == "sqr":
                result = num1 * num1
                print(num1, "sqr", "=", result)
                
            elif user_input == "cube":
                result = num1 * num1 * num1
                print(num1, "cube", "=", result)
        else:
            
            print("Invalid Input")


calculator()