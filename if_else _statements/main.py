# if= Do some code only IF some condition is True
#     Else do something else

 # This is a basic decision making system

#Sample programme 1

# name=str(input("What is your name: "))
# age=int(input("How old are you: "))

# if age >= 18:
#     print(f"The credit card has been issued to {name}")
# else:
#     print(f"{name}, You are not old enough to be given a credit card")

# Sample programme 2-Lets build a simple calculator programme

operand1=int(input("Input your first operand: "))
operand2=int(input("Input your second operand: "))
operator=str(input("Input the operator symbol: "))
results=0

if operator == '+':
    results=operand1 + operand2
    print(results)
elif operator == '-':
    results=operand1 - operand2
    print(results)
elif operator == '*':
    results= operand1 * operand2
    print(results)
elif operator == '/':
    results=operand1 / operand2
    print(results)
elif operator == '**':
    results=operand1 ** operand2
    print(results)
else:
    print(f" MATH ERROR: {operator} cannot be recognized")





