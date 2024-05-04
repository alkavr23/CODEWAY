#Program for a simple calculator

def calculation(num1, num2, operator):
  if operator == "+":
    return num1+num2
  elif operator == "-":
    return num1-num2
  elif operator == "*":
    return num1*num2
  elif operator == "/":
      if num2 == 0:
          print("Error: Division by zero")
          return None
      else:
          return num1/num2
  else:
    print("Invalid operator")
    return None
while True:
    try:
        num1=float(input("Enter the first number:"))
        num2=float(input("Enter the second number:"))
        operator=input("Select operation from +,-,* and /: \n")
    except ValueError:
       print("Invalid input. Please enter numbers only.")
       continue
   
    result = calculation(num1, num2, operator)
    if result is not None:
        print(num1,operator,num2,"=",result)
    break
    

