print('Welcome to the greatest calculator in the world ')

while True:
    
    num1 = float(input('enter your 1st no. ='))
    operator = input('enter your operator(+-/*)')
    num2 = float(input('enter your 2nd no. ='))

    if operator == "+":
        print("Your Ans =", num1 + num2)
    elif operator == "-":
        print("Your Ans =", num1 - num2)
    elif operator == "/":
        print("Your Ans =", num1 / num2)
    elif operator == "*":
        print("Your Ans =", num1 * num2)
    else:
        print("wrong input")


print("wrong input")
