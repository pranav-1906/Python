accept = input('would you like to calculate?')
while accept.lower() == 'yes':
    inp= input("Simple interest(si) or Compound interest(ci):")

    if inp.lower() == 'si':
        principle = int(input("Enter Principle:"))
        rate = int(input("Enter Rate:"))
        time = int(input("Enter No. of years:"))
        result = principle+((principle*rate*time)/100)
        print(f"The simple interest in {time} years would be:{result}")
        accept = input("would you like to calculate again?")
    
    elif inp.lower() == 'ci':
        principle = int(input("Enter Principle:"))
        rate = int(input("Enter Rate:"))
        time = int(input("Enter No. of years:"))
        result = principle * pow((1+rate/100),time)
        print(f"The compound interest in {time} years would be:{result}")
        accept = input("would you like to calculate again?")

print("gracias!")