#code 2

name=input("Enter your name: ")
if len(name)<3:
    print('name must be at least 3 characters')
elif len(name)>10:
    print('name must be at most 10 characters')
else:
    print('name is too short')
