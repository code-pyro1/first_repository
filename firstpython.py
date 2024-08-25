#my first good and working code,congratulations to me

weight = int(input("Enter your weight : "))
unit = (input("Lbs or Kg : "))
if unit== "Lbs":
    converted = int(weight) * 0.45359
    print(f'your weight in kilograms is {converted}kg')
else:
    converted = weight / 0.45359
    print(f'your weight in pounds is {converted}Lbs')
