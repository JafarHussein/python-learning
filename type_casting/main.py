# Type casting , this is the process of converting a value of one data type to another
#                (String, interger, float, boolean)
#                Explicit vs Implict

# Explicit type casting

name="Jafar Hussein"
age=21
gpa=1.9
student=True

print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

#Type casting an integer to a float
age=float(age)
print(age)

#Type casting a float to an integer
gpa=int(gpa)
print(gpa)
#Note that when you convert a float to an integer, the decimal part is truncated

student=str(student)
print(type(student))

#Typecasting a number to a boolean
age=bool(age)
print(type(age))
print(age)

#Implicit Typecasting -> a variable data type is just converted automatically
x=2
y=2.0



