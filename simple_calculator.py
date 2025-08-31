while True:
    print("--------Calculator--------")
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Square\n6.Cube\n7.Power\n8.Quit")
    choice = int(input("Enter the no. of operation you would like to perform:"))

    match choice:
        case 1:
            print("-----------------------------")
            iterate = int(input("how many no. do you want to add?"))
            result = 0
            for i in range(1, iterate+1):
               num=int(input(f"Enter num{i}:"))
            result += num
            print(f"The sum is {result}")
            print("-----------------------------")
        case 2:
            print("-----------------------------")
            num1=int(input("Enter num1:"))
            num2=int(input("Enter num2:"))
            print(f"The difference of {num1} and {num2} is {num1-num2}")
            print("-----------------------------")
        case 3:
            print("-----------------------------")
            iterate = int(input("how many no. do you want to numtiply?"))
            result = 1
            for i in range(1, iterate+1):
                num=int(input(f"Enter num{i}:"))
                result *= num
            print(f"The product is {result}")
            print("-----------------------------")
        case 4:
            print("-----------------------------")
            num1=int(input("Enter num1:"))
            num2=int(input("Enter num2:"))
            print(f"The quotient of {num1} and {num2} is {num1/num2}")
            print("-----------------------------")
        case 5:
            print("-----------------------------")
            num=int(input("Enter num:"))
            print(f"The square of {num} is {num*num}")
            print("-----------------------------")
        case 6:
            print("-----------------------------")
            num=int(input("Enter num:"))
            print(f"The cube of {num} is {num*num*num}")
            print("-----------------------------")
        case 7:
            print("-----------------------------")
            num1=int(input("Enter number:"))
            num2=int(input("Enter power:"))
            result = 1
            for i in range(1,num2+1):
                result *=num1
            print(f"{num1} to the power {num2} is {result}")
            print("-----------------------------")
        case 8:
            break
        case _:
            print("Invalid input")