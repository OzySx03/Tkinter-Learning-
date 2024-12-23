# a = 10
# b = 5
# print(f"{a} ile {b} nin çarpımı {a*b} dir.")

# Celcius = int(input("write in celcius"))
# Fahrenheit = ((Celcius * 1.8) + 32)
# print(Fahrenheit)
#def grades():
#    grade = int(input("Write your grade: "))
#    if grade > 90:
#        return("Your grade A")
#    elif 75>grade>90:
#        return("Your grade B")
#    else:
#        return("Your grade C")
#grades()


# weight = int(input("Enter your weight"))
# height = float(input("Enter your height"))
# BMI = (weight / (height ** 2))
# if BMI < 18.5:
#     print("underweight")
# elif 18.5 < BMI < 24.9:
#     print("normal")
# elif 25 < BMI < 29.9:
#     print("overweight")
# else:
#     print("Fat")


# a = [1,2,3,4,5,6,7,8,9]
# for i in a:
#     if  i%2 == 0:
#         print(f"{i} is an even number")
#     else:
#         print(f"{i} is an odd number")


# a = [1,-2,3,-4,5,-6,7,-8,9]
# a1 = []
# for i in a:
#     if i < 0:
#         a1.append(i*-1)
#     else:
#         a1.append(i)

# print(a1)


# for i in range(10, 18):
#     print(i)


# age = 20
# count = 0
# while age>18:
#     print("You can vote")
#     break
# name = input("enter your name")
# surname = input("enter your surname")
# def email(name, surname):
#     adress = name + "." + surname + "@stu.fbu.edu.tr"
#     return adress
# print(email(name, surname))


# weight = int(input("Enter your weight"))
# height = float(input("Enter your height"))
# def BMIformula(height,weight):
#     BMI = (weight / (height ** 2))
#     if BMI < 18.5:
#         return("underweight")
#     elif 18.5 < BMI < 24.9:
#         return("normal")
#     elif 25 < BMI < 29.9:
#         return("overweight")
#     else:
#         return("Fat")
    
# print(BMIformula(65,1.85))


# def formula1(Celcius):
#     Fahrenheit = ((Celcius * 1.8) + 32)
#     return Fahrenheit

# print(formula1(30))



def BMIformula(height,weight):
    BMI = (weight / (height ** 2))
    if BMI < 18.5:
        return("underweight")
    elif 18.5 < BMI < 24.9:
        return("normal")
    elif 25 < BMI < 29.9:
        return("overweight")
    else:
        return("obesity")
    
print(BMIformula(1.80,65))
