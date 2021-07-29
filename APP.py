print("Welcome to my BMI Calculator")
#This code is written by Kulbhushan Karn
print("1 - Male")
print("2 - Female")
gender = int(input("Are you a Male or Female? "))
if gender == 1:
    weight = int(input("Enter your weight in kg! "))
    hight = int(input("Enter your hight in Centimeters! "))
    result = int(weight) / int(hight * hight)
    print("Your BMI is:", result * 10000)
    if result<0.00195:
        print("You are fleshless!")
    elif result>0.0025:
            print("You are fat!")
    else:print("You are optimal!")
        


if gender == 2:
    weight = int(input("Enter you weight in kg! "))
    hight = int(input("Enter you hight is centimeters! "))
    result = int(weight) / int(hight * hight)
    print("Your BMI is:", result * 10000)
    if result<0.00185:
        print("You are fleshless!")
    elif result>0.0024:
            print("Your are fat!")
    else:
            print("Your are optimal!")
            
        
